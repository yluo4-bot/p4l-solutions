import sys


# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.

# GameBoard is a two-dimensional list of boolean variables
# representing a single generation of a Game of Life board.
GameBoard = list[list[int]]  

# write your play_automaton() function here along with any subroutines that you need.
# The Autograder will only analyze the final step of your solution. If you want to see the output of your intermediate steps, then you may print them to stdout.
def play_automaton(num_gens: int, neighborhood_type: str, initial_board: GameBoard,  
    rules: dict[str, int]) -> list[GameBoard]:

    print(type(initial_board), type(num_gens), type(neighborhood_type), type(rules))
    print(repr(initial_board)[:60], repr(num_gens), repr(neighborhood_type))


    brdLst = [initial_board]


    for i in range(num_gens):
        brdLst.append(update_board(brdLst[i], neighborhood_type, rules))

    return brdLst


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

def neighborhood_to_string(current_board: GameBoard, r: int, c: int, neighborhood_type: str) -> str:
    """
    Construct the neighborhood string for a given cell in a GameBoard.
    Args:
        current_board (GameBoard): The current game board.
        r (int): The row index of the cell.
        c (int): The column index of the cell.
        neighborhood_type (str): The type of neighborhood ("Moore" or "vonNeumann").
    Returns:
        str: A string formed of the central square followed by its neighbors
        according to the neighborhood type indicated.
    """

    neighborhood = str(current_board[r][c])

    if neighborhood_type == "Moore":
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    elif neighborhood_type == "vonNeumann":
        offsets =  [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for x,y in offsets:

        if in_field(current_board, r+x, c+y):
            neighborhood += str(current_board[r+x][c+y])

        else:
            neighborhood += "0"
    
    return neighborhood
def count_rows(board: list[list[bool]]) -> int:
    """
    Count the number of rows in a game board.

    Args:
        board: A two-dimensional array of boolean values.
    Returns:
        The number of rows in the board.
    """
    return len(board)


def count_columns(board: list[list[bool]]) -> int:
    """
    Count the number of columns in a game board.

    Args:
        board: A two-dimensional array of boolean values.
    Returns:
        The number of columns in the board.
    """
    # assume that we have a rectangular board
    if count_rows(board) == 0:
        raise Exception("Error: empty board given to count_cols")
    # give # of elements in 0-th row
    return len(board[0])

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
            
def in_field(board: GameBoard, i: int, j: int) -> bool:
    """
    Check if the indices (i, j) are within the bounds of the board.
    Args:
        board (GameBoard): The game board (2D list of ints).
        i (int): Row index.
        j (int): Column index.
    Returns:
        bool: True if (i, j) is inside the board, False otherwise.
    """
    # parameter checks
    if not isinstance(board, list) or len(board) == 0:
        raise ValueError("board must be a non-empty GameBoard.")
    if not isinstance(i, int) or not isinstance(j, int):
        raise ValueError("i and j must be integers.")
    if i < 0 or j < 0:
        return False
    if i >= count_rows(board) or j >= count_columns(board):
        return False
    # if we survive to here, then we are on the board
    return True

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
