import sys

# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.

# GameBoard is a two-dimensional list of boolean variables
# representing a single generation of a Game of Life board.
GameBoard = list[list[bool]]  

# write your update_board() function here along with any subroutines that you need.
def update_board(current_board: GameBoard) -> GameBoard:
    """
    update_board takes as input a GameBoard and returns the board resulting
    from playing the Game of Life for one generation.
    Args:
        current_board (GameBoard): The current game board.
    Returns:
        GameBoard: A new board representing the next generation.
    """

    gb = initialize_board(len(current_board), len(current_board[0]))

    for row in range(len(current_board)):
        for col in range(len(current_board[0])):
            gb[row][col] = update_cell(current_board, row, col)

    return gb

    pass


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
