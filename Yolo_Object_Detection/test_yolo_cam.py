import cv2
from ultralytics import YOLO

# Load the trained YOLO model
model = YOLO('D:/MS/Spring 2025/runs/detect/train/weights/best.pt')  # Update the path to your trained model

# Open the webcam feed (use 0 for the default camera, or 1 for an external camera)
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Error: Unable to access the camera.")
    exit()

print("Press 'q' to exit.")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read frame.")
        break

    # Run YOLO inference on the frame
    results = model(frame, conf=0.5)  # Adjust confidence threshold if needed

    # Annotate the frame with detection results
    annotated_frame = results[0].plot()  # Plot bounding boxes and labels on the frame

    # Display the annotated frame
    cv2.imshow("YOLO Detection", annotated_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
