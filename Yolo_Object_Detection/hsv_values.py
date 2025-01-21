import cv2

# cap = cv2.VideoCapture(1)
# ret, frame = cap.read()
# if ret:
#     cv2.imwrite("balloon_sample.jpg", frame)
# cap.release()


def get_hsv_values(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        hsv_value = hsv[y, x]
        print(f"HSV Value at ({x}, {y}): {hsv_value}")

# Load the image
image = cv2.imread("balloon_sample.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Display the image
cv2.imshow("Balloon Image", image)
cv2.setMouseCallback("Balloon Image", get_hsv_values)
cv2.waitKey(0)
cv2.destroyAllWindows()
