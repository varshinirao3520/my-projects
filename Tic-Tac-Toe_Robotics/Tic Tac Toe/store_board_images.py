import cv2
import os

# Create a folder to store the images
output_folder = "Only_Board_and_araku"
os.makedirs(output_folder, exist_ok=True)

# Create a VideoCapture object, specifying the camera index (0 for default camera)
# If you have multiple cameras, you may need to adjust the index accordingly.
cap = cv2.VideoCapture(2)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Counter for naming the saved images
image_counter = 0

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If the frame is read correctly, ret will be True
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Display the resulting frame
    cv2.imshow("Camera Feed", frame)

    # Save the frame as an image file in the specified folder
    image_name = os.path.join(output_folder, f"captured_image_{image_counter}.png")
    cv2.imwrite(image_name, frame)
    print(f"Saved {image_name}")

    # Increment the image counter
    image_counter += 1

    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
