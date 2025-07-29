import cv2
from ultralytics import YOLO

def main():
    # Load the pre-trained YOLOv8 nano model
    model = YOLO('yolov8n.pt')  # Automatically downloads the model if not found
    print(model.names)

    # Open default webcam (0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    print("Starting YOLOv8 real-time detection. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Run inference on the frame
        results = model(frame)

        # Annotate the frame with bounding boxes and labels
        annotated_frame = results[0].plot()

        # Show the result in a window
        cv2.imshow("YOLOv8 Real-time Detection", annotated_frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
