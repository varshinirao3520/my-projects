import cv2
import numpy as np

# Constants for the Tic Tac Toe board
ROWS = 3
COLS = 3

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

# Function to detect and mark regions where players can make moves
def mark_available_cells(frame):
    height, width, _ = frame.shape
    cell_width = width // COLS
    cell_height = height // ROWS

    for i in range(ROWS):
        for j in range(COLS):
            cv2.rectangle(frame, (j * cell_width, i * cell_height),
                          ((j + 1) * cell_width, (i + 1) * cell_height), (0, 255, 0), 2)

# Main function to play Tic Tac Toe with video camera
def play_tic_tac_toe():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Draw Tic Tac Toe board on the frame
        draw_board(frame)

        # Mark available cells where players can make moves
        mark_available_cells(frame)

        # Display the resulting frame
        cv2.imshow("Tic Tac Toe", frame)

        # Check for the 'q' key to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    play_tic_tac_toe()
