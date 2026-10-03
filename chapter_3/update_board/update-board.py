import sys

# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.

# GameBoard is a two-dimensional list of boolean variables
# representing a single generation of a Game of Life board.
GameBoard = list[list[int]]  

# write your update_board() function here along with any subroutines that you need.
def update_board(current_board: GameBoard, neighborhood_type: str, rules: dict[str, int]) ->           GameBoard:
    """
    Update a GameBoard for one generation according to the given rules and neighborhood type.
    Args:
        current_board (GameBoard): The current state of the automaton.
        neighborhood_type (str): Either "Moore" or "vonNeumann".
        rules (dict[str, int]): A mapping from neighborhood strings to next-state integers.
    Returns:
        GameBoard: The new board after applying the automaton rules for one generation.
    """
    gb = initialize_board(len(current_board), len(current_board[0]))

    for i in range(len(current_board)):
        for j in range(len(current_board[0])):
            gb[i][j] = update_cell(current_board, i, j, neighborhood_type, rules)

    return gb

    pass

def initialize_board(num_rows: int, num_cols: int) -> list[list[int]]:
    """
    Initialize a board with all cells set to 0.

    Args:
        num_rows: Number of rows in the board.
        num_cols: Number of columns in the board.
    Returns:
        A 2D list representing the board, initialized to 0.
    """
    # make a 2-D list (default values = 0)
    board = []
    # now we need to make the rows too
    for r in range(num_rows):
        board.append([0] * num_cols)

    return board
