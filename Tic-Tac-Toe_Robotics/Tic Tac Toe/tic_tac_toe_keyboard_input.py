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

# Function to draw X or O on the board
def draw_move(frame, row, col, player):
    height, width, _ = frame.shape
    cell_width = width // COLS
    cell_height = height // ROWS

    x = col * cell_width
    y = row * cell_height

    if player == 'X':
        cv2.line(frame, (x, y), (x + cell_width, y + cell_height), (0, 0, 255), 2)
        cv2.line(frame, (x + cell_width, y), (x, y + cell_height), (0, 0, 255), 2)
    elif player == 'O':
        center = (x + cell_width // 2, y + cell_height // 2)
        radius = min(cell_width, cell_height) // 2 - 5
        cv2.circle(frame, center, radius, (0, 0, 255), 2)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows and columns
    for i in range(ROWS):
        if all(board[i][j] == player for j in range(COLS)) or all(board[j][i] == player for j in range(ROWS)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(ROWS)) or all(board[i][ROWS - 1 - i] == player for i in range(ROWS)):
        return True

    return False

# Function to check if the board is full (a draw)
def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(ROWS) for j in range(COLS))

# Function to get available moves on the board
def get_available_moves(board):
    return [(i, j) for i in range(ROWS) for j in range(COLS) if board[i][j] == ' ']

# Minimax algorithm for AI move
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for move in get_available_moves(board):
            row, col = move
            board[row][col] = 'O'
            eval = minimax(board, depth + 1, False)
            board[row][col] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_available_moves(board):
            row, col = move
            board[row][col] = 'X'
            eval = minimax(board, depth + 1, True)
            board[row][col] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move for the AI
def find_best_move(board):
    best_val = float('-inf')
    best_move = None

    for move in get_available_moves(board):
        row, col = move
        board[row][col] = 'O'
        move_val = minimax(board, 0, False)
        board[row][col] = ' '

        if move_val > best_val:
            best_move = move
            best_val = move_val

    return best_move

# Main function to play Tic Tac Toe against AI
def play_tic_tac_toe():
    cap = cv2.VideoCapture(0)
    board = initialize_board()
    player_turn = True  # True for player X, False for player O

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Draw Tic Tac Toe board on the frame
        draw_board(frame)

        # Draw X or O based on player's turn
        if player_turn:
            cv2.putText(frame, "Player X's turn", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        else:
            cv2.putText(frame, "Player O's turn", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        # Detect keyboard input to make a move
        key = cv2.waitKey(1) & 0xFF

        if key == 27:  # Press 'Esc' to exit
            break

        if key == ord(' ') and player_turn:  # Press 'Space' to make a move for Player X
            row, col = get_move_from_keyboard()
            if board[row][col] == ' ':
                board[row][col] = 'X'
                player_turn = not player_turn

        # AI makes a move for Player O
        if not player_turn:
            best_move = find_best_move(board)
            if best_move:
                row, col = best_move
                board[row][col] = 'O'
                player_turn = not player_turn

        # Draw X or O on the board
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] != ' ':
                    draw_move(frame, i, j, board[i][j])

        # Display the resulting frame
        cv2.imshow("Tic Tac Toe", frame)

        # Check for game over conditions
        if check_winner(board, 'X'):
            print("Player X wins!")
            break
        elif check_winner(board, 'O'):
            print("Player O wins!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to get player's move from keyboard input
def get_move_from_keyboard():
    print("Enter row and column (separated by space):")
    move = input().split()
    row, col = map(int, move)
    return row, col

if __name__ == "__main__":
    play_tic_tac_toe()