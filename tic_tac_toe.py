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

display_instruct()

input("\nPress Enter to exit the program.")