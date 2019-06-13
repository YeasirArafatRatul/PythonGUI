"""Tic Tac Toe"""


# Game-Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]

game_still_going = True  # Global-Variable

winner = None

current_player = "Player 1"


def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")


def start():
    display_board()

    while game_still_going:

        handle_turn(current_player)

        #"""Check if game is still going"""
        check_if_game_over()

        #"""flip to the other player"""
        flip_player()

    if winner == "Player 1" or winner == "Player 2":
        print(winner+"WoN")
    elif winner == None:
        print("Game Tied")


# Display the game board to the screen


def handle_turn(player):

    global current_player

    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    # Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid = False
    while not valid:

        # Make sure the input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        # Get correct index in our board list
        position = int(position) - 1
        if board[position] == "-":
            valid = True

        else:
            print("Invalid Choice")

    if current_player == "Player 1":
        board[position] = "X"
    else:
        board[position] = "O"

    display_board()


def check_if_game_over():

    check_for_winner()

    check_if_tie()


def check_for_winner():
    # """set up global variables"""
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    # Get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner

    else:
        winner = None


def check_rows():

    global game_still_going

    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        game_still_going = False

# """Return the Winner"""

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    else:
        return None


def check_columns():
    global game_still_going
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"

    if column1 or column2 or column3:
        game_still_going = False


# """Return the Winner"""
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]

    else:
        return None


def check_diagonals():

    global game_still_going

    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"

    if diagonal1 or diagonal2:
        game_still_going = False


# """Return the Winner"""
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[6]
    else:
        return None


def check_if_tie():

    global game_still_going

    if "-" not in board:
        game_still_going = False

    else:
        return False


def flip_player():

    global current_player

    """flip flop"""
    if current_player == "Player 1":
        current_player = "Player 2"
    elif current_player == "Player 2":
        current_player = "Player 1"

    return


# ------------ Start Execution -------------
start()
