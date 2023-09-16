# script to prevent double counting of fish using yolov8

import argparse
from typing import Dict, List, Set, Tuple

import cv2
import numpy as np
from tqdm import tqdm
from ultralytics import YOLO

import supervision as sv

COLORS = sv.ColorPalette.default()

ZONE_IN_POLYGONS = [
    np.array([[592, 282], [900, 282], [900, 82], [592, 82]]),
    np.array([[950, 860], [1250, 860], [1250, 1060], [950, 1060]]),
    np.array([[592, 582], [592, 860], [392, 860], [392, 582]]),
    np.array([[1250, 282], [1250, 530], [1450, 530], [1450, 282]]),
]

ZONE_OUT_POLYGONS = [
    np.array([[950, 282], [1250, 282], [1250, 82], [950, 82]]),
    np.array([[592, 860], [900, 860], [900, 1060], [592, 1060]]),
    np.array([[592, 282], [592, 550], [392, 550], [392, 282]]),
    np.array([[1250, 860], [1250, 560], [1450, 560], [1450, 860]]),
]


class DetectionsManager:
    def __init__(self, reentry_threshold: int, frame_height: int, buffer_ratio: float = 0.1) -> None:
        self.tracker_id_to_timestamp: Dict[int, int] = {}
        self.reentry_candidates: Set[int] = set()
        self.reentry_threshold = reentry_threshold
        self.buffer_zone = frame_height - int(frame_height * buffer_ratio)

    def update(self, detections_all: sv.Detections, current_timestamp: int) -> int:
        # Check for fish entering the top buffer zone
        for tracker_id, bbox in zip(detections_all.tracker_id, detections_all.bbox):
            if bbox[1] <= self.buffer_zone:  # Assuming bbox format is [x, y, w, h]
                self.reentry_candidates.add(tracker_id)

        # Count unique fish in the current frame
        unique_fish_count = 0
        for tracker_id in detections_all.tracker_id:
            if tracker_id not in self.tracker_id_to_timestamp:
                # If it's a new fish or an old fish re-entering after the threshold
                if tracker_id not in self.reentry_candidates or (current_timestamp - self.tracker_id_to_timestamp[tracker_id] > self.reentry_threshold):
                    unique_fish_count += 1
            self.tracker_id_to_timestamp[tracker_id] = current_timestamp

        # Clear old tracker IDs periodically for efficiency
        inactive_trackers = [tid for tid, timestamp in self.tracker_id_to_timestamp.items() if current_timestamp - timestamp > self.reentry_threshold * 2]
        for tid in inactive_trackers:
            del self.tracker_id_to_timestamp[tid]
            self.reentry_candidates.discard(tid)

        return unique_fish_count

# The buffer_zone defines the starting y-coordinate of the top buffer zone.
# The reentry_candidates set keeps track of fish that enter the top buffer zone.
# The tracker_id_to_timestamp dictionary maps each tracker ID to the last timestamp it was seen.
# The update method checks for fish entering the top buffer zone, counts unique fish considering potential re-entries, and periodically clears old tracker IDs.

def initiate_polygon_zones(
    polygons: List[np.ndarray],
    frame_resolution_wh: Tuple[int, int],
    triggering_position: sv.Position = sv.Position.CENTER,
) -> List[sv.PolygonZone]:
    return [
        sv.PolygonZone(
            polygon=polygon,
            frame_resolution_wh=frame_resolution_wh,
            triggering_position=triggering_position,
        )
        for polygon in polygons
    ]


class VideoProcessor:
    def __init__(
        self,
        source_weights_path: str,
        source_video_path: str,
        target_video_path: str = None,
        confidence_threshold: float = 0.3,
        iou_threshold: float = 0.7,
    ) -> None:
        self.conf_threshold = confidence_threshold
        self.iou_threshold = iou_threshold
        self.source_video_path = source_video_path
        self.target_video_path = target_video_path

        self.model = YOLO(source_weights_path)
        self.tracker = sv.ByteTrack()

        self.video_info = sv.VideoInfo.from_video_path(source_video_path)
        self.zones_in = initiate_polygon_zones(
            ZONE_IN_POLYGONS, self.video_info.resolution_wh, sv.Position.CENTER
        )
        self.zones_out = initiate_polygon_zones(
            ZONE_OUT_POLYGONS, self.video_info.resolution_wh, sv.Position.CENTER
        )

        self.box_annotator = sv.BoxAnnotator(color=COLORS)
        self.trace_annotator = sv.TraceAnnotator(
            color=COLORS, position=sv.Position.CENTER, trace_length=100, thickness=2
        )
        self.detections_manager = DetectionsManager()

    def process_video(self):
        frame_generator = sv.get_video_frames_generator(
            source_path=self.source_video_path
        )

        if self.target_video_path:
            with sv.VideoSink(self.target_video_path, self.video_info) as sink:
                for frame in tqdm(frame_generator, total=self.video_info.total_frames):
                    annotated_frame = self.process_frame(frame)
                    sink.write_frame(annotated_frame)
        else:
            for frame in tqdm(frame_generator, total=self.video_info.total_frames):
                annotated_frame = self.process_frame(frame)
                cv2.imshow("Processed Video", annotated_frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            cv2.destroyAllWindows()

    def annotate_frame(
        self, frame: np.ndarray, detections: sv.Detections
    ) -> np.ndarray:
        annotated_frame = frame.copy()
        for i, (zone_in, zone_out) in enumerate(zip(self.zones_in, self.zones_out)):
            annotated_frame = sv.draw_polygon(
                annotated_frame, zone_in.polygon, COLORS.colors[i]
            )
            annotated_frame = sv.draw_polygon(
                annotated_frame, zone_out.polygon, COLORS.colors[i]
            )

        labels = [f"#{tracker_id}" for tracker_id in detections.tracker_id]
        annotated_frame = self.trace_annotator.annotate(annotated_frame, detections)
        annotated_frame = self.box_annotator.annotate(
            annotated_frame, detections, labels
        )

        for zone_out_id, zone_out in enumerate(self.zones_out):
            zone_center = sv.get_polygon_center(polygon=zone_out.polygon)
            if zone_out_id in self.detections_manager.counts:
                counts = self.detections_manager.counts[zone_out_id]
                for i, zone_in_id in enumerate(counts):
                    count = len(self.detections_manager.counts[zone_out_id][zone_in_id])
                    text_anchor = sv.Point(x=zone_center.x, y=zone_center.y + 40 * i)
                    annotated_frame = sv.draw_text(
                        scene=annotated_frame,
                        text=str(count),
                        text_anchor=text_anchor,
                        background_color=COLORS.colors[zone_in_id],
                    )

        return annotated_frame

    def process_frame(self, frame: np.ndarray) -> np.ndarray:
        results = self.model(
            frame, verbose=False, conf=self.conf_threshold, iou=self.iou_threshold
        )[0]
        detections = sv.Detections.from_ultralytics(results)
        detections.class_id = np.zeros(len(detections))
        detections = self.tracker.update_with_detections(detections)

        detections_in_zones = []
        detections_out_zones = []

        for i, (zone_in, zone_out) in enumerate(zip(self.zones_in, self.zones_out)):
            detections_in_zone = detections[zone_in.trigger(detections=detections)]
            detections_in_zones.append(detections_in_zone)
            detections_out_zone = detections[zone_out.trigger(detections=detections)]
            detections_out_zones.append(detections_out_zone)

        detections = self.detections_manager.update(
            detections, detections_in_zones, detections_out_zones
        )
        return self.annotate_frame(frame, detections)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Fish Count with YOLO and ByteTrack"
    )

    parser.add_argument(
        "--source_weights_path",
        required=True,
        help="Path to the source weights file",
        type=str,
    )
    parser.add_argument(
        "--source_video_path",
        required=True,
        help="Path to the source video file",
        type=str,
    )
    parser.add_argument(
        "--target_video_path",
        default=None,
        help="Path to the target video file (output)",
        type=str,
    )
    parser.add_argument(
        "--confidence_threshold",
        default=0.3,
        help="Confidence threshold for the model",
        type=float,
    )
    parser.add_argument(
        "--iou_threshold", default=0.7, help="IOU threshold for the model", type=float
    )

    args = parser.parse_args()
    processor = VideoProcessor(
        source_weights_path=args.source_weights_path,
        source_video_path=args.source_video_path,
        target_video_path=args.target_video_path,
        confidence_threshold=args.confidence_threshold,
        iou_threshold=args.iou_threshold,
    )
    processor.process_video()
