# YOLO-Object-detection

# YOLOv8 Real-Time Object Detection with Webcam

This project uses [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) and OpenCV to perform real-time object detection from a webcam feed.

Example :[YOLOv8 Detection Demo](https://github.com/ultralytics/assets/raw/main/yolov8/example-output.jpg)

**FEATURES**

- Real-time object detection using YOLOv8 Nano 
- Live webcam feed with bounding boxes and labels
- Runs on CPU (or GPU if available)
  
**ULTRALYTICS COVERS**
- torch (PyTorch)
- numpy
- matplotlib
- tqdm
- Other internal YOLO utilities
- So you don’t need to add torch or numpy manually — ultralytics handles it.

**SETUP ENVIRONMENT**

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

**INSTALL DEPENDENCIES**

```bash
pip install -r requirements.txt
```

**TO RUN**

```bash
python3 yolo_webcam.py
```

