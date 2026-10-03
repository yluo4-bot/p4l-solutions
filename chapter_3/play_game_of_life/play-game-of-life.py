# import necessary libraries
import sys

# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.

# GameBoard is a two-dimensional list of boolean variables
# representing a single generation of a Game of Life board.
GameBoard = list[list[bool]]  

# write your play_game_of_life() function here along with any subroutines that you need.
# The AutoGrader will only analyze the final step of your solution. If you want to see the output of your intermediate steps, then you may print them to stdout.
def play_game_of_life(initial_board: GameBoard, num_gens: int) -> list[GameBoard]:
    """
    Simulate the Game of Life for a number of generations.

    Args:
        board: A 2D list of booleans representing the initial Game of Life board.
        num_gens: Number of generations to simulate.
    Returns:
        A list of GameBoard states of length num_gens + 1, starting with
        the initial board and followed by each successive generation.
    """

    lstBrd = [initial_board]

    for i in range(num_gens):
        lstBrd.append(update_board(lstBrd[i]))

    return lstBrd

def initialize_board(num_rows: int, num_cols: int) -> list[list[bool]]:
    """
    Initialize a board with all cells set to False.

    Args:
        num_rows: Number of rows in the board.
        num_cols: Number of columns in the board.
    Returns:
        A 2D list representing the board, initialized to False.
    """
    b = [[False] * num_cols for _ in range(num_rows)]
    return b

def assert_rectangular(board: GameBoard) -> None:
    """
    Check whether a GameBoard is rectangular.
    Args:
        board (GameBoard): The game board.
    Raises:
        ValueError: If the board has no rows or if its rows are not the same length.
    """
    if len(board) == 0:
        raise ValueError("Error: no rows in GameBoard.")
    first_row_length = len(board[0])

    # range over rows and make sure that they have the same length as first row
    for row in board:
        if len(row) != first_row_length:
            raise ValueError("Error: GameBoard is not rectangular.")
            
