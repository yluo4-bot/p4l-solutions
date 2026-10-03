# import necessary libraries
import sys
import re

# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.

# GameBoard is a two-dimensional list of boolean variables
# representing a single generation of a Game of Life board.
GameBoard = list[list[int]]  

# write your update_cell() function here along with any subroutines that you need.
def update_cell(board: GameBoard, r: int, c: int,
                neighborhood_type: str,
                rules: dict[str, int]) -> int:
    """
    Determine next-state integer for cell (r, c) using rules and neighborhood type.
    Args:
        board (GameBoard): Current state of the automaton.
        r (int): Row index of the cell to update.
        c (int): Column index of the cell to update.
        neighborhood_type (str): Either "Moore" or "vonNeumann".
        rules (dict[str, int]): A mapping from neighborhood strings to next-state integers.
    Returns:
        int: next state for the cell.
    """
    ns = neighborhood_to_string(board, r, c, neighborhood_type)

    if ns in rules: 
        return rules[ns]

    return 0
            
