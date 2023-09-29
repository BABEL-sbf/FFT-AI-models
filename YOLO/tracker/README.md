## YOLO + ByteTack

This code has a way to prevent double and overcounting of fish while conducting survey analysis.

Here's a breakdown of the script's logic:

1. **Initialization of Zones**: 
   - `ZONE_IN_POLYGONS` and `ZONE_OUT_POLYGONS` are predefined polygons that represent areas of interest in the video frame. These might be areas where fish enter or exit the frame.

2. **DetectionsManager Class**: 
   - This class is responsible for managing detected fish and ensuring that fish are not double-counted. It uses a buffer zone at the top of the frame to monitor fish that might re-enter the frame. Fish that enter this buffer zone are considered as potential re-entries.
   - The `update` method of this class checks for fish entering the buffer zone, counts unique fish considering potential re-entries, and periodically clears old tracker IDs to maintain efficiency.

3. **VideoProcessor Class**: 
   - This class is the main processing unit. It initializes the YOLO model for detection and ByteTrack for tracking.
   - The `process_video` method goes through each frame of the video, detects and tracks fish, and annotates the frame with the detected fish and their counts.
   - The `annotate_frame` method is responsible for drawing the detected fish and their counts on the frame.

4. **Main Execution**:
   - The script uses `argparse` to get command-line arguments such as paths to the source weights file, source video, target video, and some model parameters.
   - It then initializes the `VideoProcessor` class with these arguments and processes the video.

## ⚙️ parameters

| parameter                | required | description                                                                       |
|:-------------------------|:--------:|:----------------------------------------------------------------------------------|
| `--source_weights_path`  |    ✓     | Path to the source weights file for YOLOv8.                                       |
| `--source_video_path`    |    ✓     | Path to the source video file to be processed.                                    |
| `--target_video_path`    |    ✓     | Path to the target video file (output).                                           |
| `--confidence_threshold` |    ✗     | Confidence threshold for YOLO model detection. Default is 0.3.                    |
| `--iou_threshold`        |    ✗     | IOU (Intersection over Union) threshold for YOLO model detection. Default is 0.7. |

## Running the code

```bash
python tracker.py \
--source_weights_path {get weights from yolov8 model} \
--source_video_path {video.mov file} \
--confidence_threshold 0.3 \
--iou_threshold 0.5 \
--target_video_path {video_result.mov file}
```


