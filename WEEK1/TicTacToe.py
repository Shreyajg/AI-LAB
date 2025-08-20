import random

EMPTY = " "
HUMAN = "X"
COMP = "O"

def new_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]

def print_board(board):
    print("\n 0 1 2")
    for r in range(3):
        row = " | ".join(board[r])
        print(f"{r} {row}")
        if r < 2:
            print(" ---------")
    print()

def check_winner(board, mark):
    # rows
    for r in range(3):
        if all(board[r][c] == mark for c in range(3)):
            return True
    # cols
    for c in range(3):
        if all(board[r][c] == mark for r in range(3)):
            return True
    # diags
    if all(board[i][i] == mark for i in range(3)):
        return True
    if all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False

def empty_cells(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == EMPTY]

def human_move(board):
    while True:
        try:
            raw = input("Enter row and col (0-2 0-2): ").strip()
            r_s, c_s = raw.split()
            r, c = int(r_s), int(c_s)
            if r not in range(3) or c not in range(3):
                print("Out of range. Use 0, 1, or 2.")
                continue
            if board[r][c] != EMPTY:
                print("That spot is taken. Try again.")
                continue
            board[r][c] = HUMAN
            return
        except ValueError:
            print("Please enter two numbers like: 0 2")

def computer_move(board):
    r, c = random.choice(empty_cells(board))
    board[r][c] = COMP
    print(f"Computer played: {r} {c}")

def tic_tac_toe():
    board = new_board()
    print("You are X. Computer is O.")
    print_board(board)
    won=False
    while ( not won):
        # Human turn
        human_move(board)
        print_board(board)
        if check_winner(board, HUMAN):
            print("User won!")
            won=True
            return
        if not empty_cells(board):
            print("It's a draw.")
            won=True
            return

        # Computer turn
        computer_move(board)
        print_board(board)
        if check_winner(board, COMP):
            print("Computer won!")
            return
        if not empty_cells(board):
            print("It's a draw.")
            return

if __name__ == "__main__":
