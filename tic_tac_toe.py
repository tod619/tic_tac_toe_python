# Tic-Tac-Toe
# A game of Tic-Tac-Toe against a computer based oppenent
# The game uses a simple A.I model to pick counter moves against a human oppenent
# 17/05/2023

# Global Constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def display_instruct():
    """Display game instructions"""
    print(
        """
        Welcome to the game of Tic-Tac-Toe.
        This is a showdown of human intellect vs the raw computing power of the sillicon processor.

        You will make your move known by entering a number 0 - 8.  The number will correspond to the board position below:

            0 | 1 | 2
            ---------
            3 | 4 | 5
            ---------
            6 | 7 | 8
        
        Prepare yourself. The ultimate battle of brains is about to begin.
        """
    )

def ask_yes_no(question):
    """Ask the user a yes or no question"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Ask for a number within a range"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    """Determine who goes first and assign play pieces based on this choice"""
    go_first = ask_yes_no("Do you require the first move? (y/n): ")
    
    if go_first == "y":
        print("\nThe player has decided to go first this time.")
        human = X
        computer = O
    else:
        print("\nThe computer will go first this time.")
        computer = X
        human = 0
    
    return computer, human

def new_board():
    """Create new game board"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Display Game board on the screen"""
    print(f"\n\t {board[0]} | {board[1]} | {board[2]}")
    print("\t","---------")
    print(f"\t {board[3]} | {board[4]} | {board[5]}")
    print("\t","---------")
    print(f"\t {board[6]} | {board[7]} | {board[8]}")

def legal_moves(board):
    """Create a list of all the available legal moves left"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    
    return moves

def winner(board):
    """Determine the game winner"""
    WAYS_TO_WIN = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        
    if EMPTY not in board:
        return TIE
    
    return None

def human_move(board, human):
    """Get Player Move"""
    legal = legal_moves(board)
    move = None

    while move not in legal:
        move = ask_number("Where will you move? (0 - 8): ", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already occupied.")
    
    print("Fine...")
    return move


# START: TEST SECTION
#display_instruct()
# quess = ask_yes_no("Is it yes or is it no?: ")
# print(quess)
# range includes low + excludes high (low = 1 high = 10 accepts a number between 1 - 9)
# quess = ask_number("Give me a number between 1 - 10", 1, 10)
# print(quess)
# players = pieces()
# print(players)
# print(new_board())
# game_board = new_board()
# display_board(game_board)
game_board = new_board()
# player = pieces()
# print(legal_moves(game_board))
# print(winner(game_board))
# human_move(game_board, player)
# END: TEST SECTION

input("\nPress Enter to exit the program.")