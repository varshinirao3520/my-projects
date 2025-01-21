import cv2
import numpy as np

# Constants for the Tic Tac Toe board
ROWS = 3
COLS = 3

# Function to initialize an empty board
def initialize_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

# Function to draw the Tic Tac Toe board on the frame
def draw_board(frame):
    height, width, _ = frame.shape
    cell_width = width // COLS
    cell_height = height // ROWS

    # Draw horizontal lines
    for i in range(1, ROWS):
        cv2.line(frame, (0, i * cell_height), (width, i * cell_height), (255, 255, 255), 2)

    # Draw vertical lines
    for j in range(1, COLS):
        cv2.line(frame, (j * cell_width, 0), (j * cell_width, height), (255, 255, 255), 2)

# Function to detect X and O moves
def detect_moves(frame, board):
    height, width, _ = frame.shape
    cell_width = width // COLS
    cell_height = height // ROWS

    for i in range(ROWS):
        for j in range(COLS):
            x = j * cell_width
            y = i * cell_height
            roi = frame[y:y + cell_height, x:x + cell_width]

            # Convert the region of interest to grayscale
            gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

            # Apply thresholding to segment the marker
            _, thresh = cv2.threshold(gray_roi, 127, 255, cv2.THRESH_BINARY)

            # Find contours in the thresholded image
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Check if a contour is found (marker is detected)
            if contours:
                area = cv2.contourArea(contours[0])

                # Threshold for considering a contour as a marker
                marker_area_threshold = 500

                if area > marker_area_threshold:
                    # Mark X or O on the board based on the contour area
                    board[i][j] = 'X' if area > marker_area_threshold * 2 else 'O'

                    # Draw a rectangle around the detected marker
                    cv2.rectangle(frame, (x, y), (x + cell_width, y + cell_height), (0, 255, 0), 2)

# Main function to play Tic Tac Toe with video camera
def play_tic_tac_toe():
    cap = cv2.VideoCapture(0)
    board = initialize_board()

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Draw Tic Tac Toe board on the frame
        draw_board(frame)

        # Detect X and O moves
        detect_moves(frame, board)

        # Display the resulting frame
        cv2.imshow("Tic Tac Toe", frame)

        # Check for the 'q' key to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    play_tic_tac_toe()
