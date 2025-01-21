import cv2
import numpy as np

# Define the HSV range for lavender color (adjust these values based on your balloon)
LOWER_HSV = np.array([142, 147, 196])  # Replace with your actual lower HSV range
UPPER_HSV = np.array([150, 203, 255])  # Replace with your actual upper HSV range

def preprocess_frame(frame):
    """
    Preprocess the frame to normalize lighting conditions.
    """
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Apply histogram equalization for better contrast
    equalized = cv2.equalizeHist(gray)
    # Convert back to BGR (for consistent color processing)
    preprocessed = cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)
    return preprocessed

def detect_lavender_balloon(frame):
    """
    Detect lavender balloons in the frame and visualize the mask.
    """
    # Preprocess the frame for better lighting consistency
    preprocessed_frame = preprocess_frame(frame)
    
    # Convert to HSV color space
    hsv = cv2.cvtColor(preprocessed_frame, cv2.COLOR_BGR2HSV)
    
    # Create a mask for the lavender color
    mask = cv2.inRange(hsv, LOWER_HSV, UPPER_HSV)
    cv2.imshow("Raw Mask", mask)  # Debug: Show raw mask

    # Reduce noise with Gaussian blur
    mask = cv2.GaussianBlur(mask, (15, 15), 0)
    cv2.imshow("Blurred Mask", mask)  # Debug: Show blurred mask

    # Apply morphological operations to close gaps
    kernel = np.ones((7, 7), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Processed Mask", mask)  # Debug: Show processed mask

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    detected = False
    largest_contour = None

    for contour in contours:
        # Filter based on contour area (ignore very small or very large objects)
        area = cv2.contourArea(contour)
        if area < 500 or area > 10000:  # Adjust thresholds as needed
            continue

        # Filter based on shape (aspect ratio close to 1 for circular objects)
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = float(w) / h
        if aspect_ratio < 0.6 or aspect_ratio > 1.4:
            continue

        # Debugging: Print contour area and aspect ratio
        print(f"Detected contour area: {area}, Aspect ratio: {aspect_ratio}")

        # Mark this contour as the largest matching balloon
        if largest_contour is None or area > cv2.contourArea(largest_contour):
            largest_contour = contour
            detected = True

    if detected and largest_contour is not None:
        # Draw the bounding box and label on the frame
        x, y, w, h = cv2.boundingRect(largest_contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.putText(frame, "Lavender Balloon", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    
    return frame, mask

def main():
    """
    Main function to capture video from the USB camera and detect lavender balloons.
    """
    # Open the USB camera (change index if necessary)
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("[ERROR] Unable to access the camera.")
        return

    print("[INFO] Press 'q' to quit.")

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Failed to grab a frame.")
            break

        # Detect lavender balloons
        output_frame, mask = detect_lavender_balloon(frame)

        # Display the detection result
        cv2.imshow("Balloon Detection", output_frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
