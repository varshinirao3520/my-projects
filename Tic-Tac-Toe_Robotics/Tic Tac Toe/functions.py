import cv2
import numpy as np

#

# Constants
GRID_SIZE = 3
SQUARE_SIZE = 100
PLAYER_MARKER = 1
AI_MARKER = 2
EMPTY_MARKER = 0

# Initialize the game board
board = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

# Function to draw the grid
def draw_grid(frame):
    for i in range(1, GRID_SIZE):
        cv2.line(frame, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, GRID_SIZE * SQUARE_SIZE), (255, 255, 255), 2)
        cv2.line(frame, (0, i * SQUARE_SIZE), (GRID_SIZE * SQUARE_SIZE, i * SQUARE_SIZE), (255, 255, 255), 2)

# Function to draw the X and O markers
def draw_markers(frame):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i, j] == PLAYER_MARKER:
                cv2.putText(frame, 'X', (j * SQUARE_SIZE + 30, i * SQUARE_SIZE + 70),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3, cv2.LINE_AA)
            elif board[i, j] == AI_MARKER:
                cv2.putText(frame, 'O', (j * SQUARE_SIZE + 30, i * SQUARE_SIZE + 70),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3, cv2.LINE_AA)

# Function to check for a win
def check_winner():
    # Check rows and columns
    for i in range(GRID_SIZE):
        if np.all(board[i, :] == PLAYER_MARKER) or np.all(board[:, i] == PLAYER_MARKER):
            return "Player wins!"
        elif np.all(board[i, :] == AI_MARKER) or np.all(board[:, i] == AI_MARKER):
            return "AI wins!"

    # Check diagonals
    if np.all(np.diag(board) == PLAYER_MARKER) or np.all(np.diag(np.fliplr(board)) == PLAYER_MARKER):
        return "Player wins!"
    elif np.all(np.diag(board) == AI_MARKER) or np.all(np.diag(np.fliplr(board)) == AI_MARKER):
        return "AI wins!"

    # Check for a tie
    if not any(EMPTY_MARKER in row for row in board):
        return "It's a tie!"

    return None

# Function to make a move in the game
def make_move(row, col, marker):
    if board[row, col] == EMPTY_MARKER:
        board[row, col] = marker
        return True
    return False

# Main loop
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Draw the game grid
    draw_grid(frame)

    # Get the player's move from mouse click (assuming a 3x3 grid)
    _, thresh = cv2.threshold(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 200, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # for contour in contours:
    #     area = cv2.contourArea(contour)
    #     if area > 500:
    #         x, y, w, h = cv2.boundingRect(contour)
    #         row = y // SQUARE_SIZE
    #         col = x // SQUARE_SIZE

    #         if make_move(row, col, PLAYER_MARKER):
    #             result = check_winner()
    #             if result:
    #                 print(result)
    #                 board = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    #             else:
    #                 # Implement AI move (random for simplicity)
    #                 available_moves = np.argwhere(board == EMPTY_MARKER)
    #                 if len(available_moves) > 0:
    #                     ai_move = available_moves[np.random.choice(len(available_moves))]
    #                     make_move(ai_move[0], ai_move[1], AI_MARKER)

    # Draw X and O markers
    draw_markers(frame)

    cv2.imshow('Tic Tac Toe', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()