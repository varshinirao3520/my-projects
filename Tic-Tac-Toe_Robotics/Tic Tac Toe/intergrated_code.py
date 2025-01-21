import cv2
import numpy as np
import alpha_beta as ab
import random

ROWS = 3
COLS = 3

class Tic(object):
    winning_combos = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6])
    winners = ('X-win', 'Draw', 'O-win')

    def __init__(self, squares=[]):
        """Initialize either custom or deafult board"""
        if len(squares) == 0:
            self.squares = [None for i in range(9)]
        else:
            self.squares = squares

    def show(self):
        """Print game progress"""
        for element in [
                self.squares[i: i + 3] for i in range(0, len(self.squares), 3)]:
            print(element)

    

    def available_moves(self):
        return [k for k, v in enumerate(self.squares) if v is None]

    def available_combos(self, player):
        return self.available_moves() + self.get_squares(player)

    def complete(self):
        """Check if game has ended"""
        if None not in [v for v in self.squares]:
            return True
        if self.winner() is not None:
            return True
        return False

    def X_won(self):
        return self.winner() == 'X'

    def O_won(self):
        return self.winner() == 'O'

    def tied(self):
        return self.complete() and self.winner() is None

    def winner(self):
        for player in ('X', 'O'):
            positions = self.get_squares(player)
            for combo in self.winning_combos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player
        return None

    def get_squares(self, player):
        """Returns squares belonging to a player"""
        return [k for k, v in enumerate(self.squares) if v == player]

    def make_move(self, position, player):
        self.squares[position] = player

    def alphabeta(self, node, player, alpha, beta):
        """Alphabeta algorithm"""
        if node.complete():
            if node.X_won():
                return -1
            elif node.tied():
                return 0
            elif node.O_won():
                return 1

        for move in node.available_moves():
            node.make_move(move, player)
            val = self.alphabeta(node, get_enemy(player), alpha, beta)
            node.make_move(move, None)
            if player == 'O':
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta
            else:
                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha
        return alpha if player == 'O' else beta
    # ... (code for the Tic class from the previous code snippet)

def get_enemy(player):
    if player == 'X':
        return 'O'
    return 'X'

def initialize_board():
        return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

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

def determine(board, player):
    """Determine best possible move"""
    a = -2
    choices = []
    if len(board.available_moves()) == 9:
        return 4
    for move in board.available_moves():
        board.make_move(move, player)
        val = board.alphabeta(board, get_enemy(player), -2, 2)
        board.make_move(move, None)
        if val > a:
            a = val
            choices = [move]
        elif val == a:
            choices.append(move)
    return random.choice(choices)# ... (code for the determine function from the previous code snippet)

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

def play_tic_tac_toe():
    board = Tic()
    board.show()

    while not board.complete():
        player = 'X'
        player_move = int(input('Next Move: ')) - 1
        if player_move not in board.available_moves():
            continue
        board.make_move(player_move, player)
        board.show()

        if board.complete():
            break
        player = get_enemy(player)
        computer_move = determine(board, player)
        board.make_move(computer_move, player)
        board.show()
    print('Winner is', board.winner())

def play_tic_tac_toe_with_camera():
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

def get_move_from_keyboard():
    print("Enter row and column (separated by space):")
    move = input().split()
    row, col = map(int, move)
    return row, col

if __name__ == '__main__':
    choice = input("Choose mode: '1' for camera-based Tic Tac Toe, '2' for command-line Tic Tac Toe: ")
    if choice == '1':
        play_tic_tac_toe_with_camera()
    elif choice == '2':
        play_tic_tac_toe()
    else:
        print("Invalid choice")
