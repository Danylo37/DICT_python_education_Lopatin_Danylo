"""TicTacToe project"""
import sys


def print_board(game_board):
    """
       Printing TicTacToe board

       Parameters:
       game_board (string): TicTacToe board
    """
    print("---------")
    for row in game_board:
        row = " ".join(row)
        print(f"| {row} |")
    print("---------")


def is_correct_input(u_input):
    """
       Checking if the input is correct

       Parameters:
       u_input (string): user's input

       Returns:
       boolean True - if the input is correct
       boolean False - if it isn't correct
    """
    try:
        x, y = map(int, u_input.split())

        if not (1 <= x <= 3 and 1 <= y <= 3):
            print("Coordinates should be from 1 to 3!")
            return False

        if board[x - 1][y - 1] != '_':
            print("This cell is occupied! Choose another one!")
            return False

    except ValueError:
        print("You should enter numbers!")
        return False

    return True


def get_winner(game_board):
    """
       Checking if there is a winner

       Parameters:
       game_board (string): TicTacToe board

       Returns:
       game_winner (string): winner's mark ("X" or "O")
       None if there is no winner
    """
    game_winner = None
    for index in range(3):
        # Horizontal lines check
        if game_board[index][0] == game_board[index][1] == game_board[index][2] != '_':
            game_winner = game_board[index][0]

        # Vertical lines check
        if game_board[0][index] == game_board[1][index] == game_board[2][index] != '_':
            game_winner = game_board[0][index]

    # Diagonals check
    if game_board[0][0] == game_board[1][1] == game_board[2][2] != '_':
        game_winner = game_board[0][0]
    if game_board[0][2] == game_board[1][1] == game_board[2][0] != '_':
        game_winner = game_board[0][2]

    return game_winner


board = [["_", "_", "_"],
         ["_", "_", "_"],
         ["_", "_", "_"]]
current_player = "X"

print_board(board)

moves = 9
for i in range(moves):
    while True:
        user_input = input("Enter the coordinates: ")

        if is_correct_input(user_input):
            coord_1, coord_2 = map(int, user_input.split())
            break

    board[coord_1 - 1][coord_2 - 1] = current_player
    print_board(board)

    winner = get_winner(board)
    if winner is not None:
        print(f"{winner} wins")
        sys.exit()

    current_player = "X" if current_player == "O" else "O"

print("Draw")
