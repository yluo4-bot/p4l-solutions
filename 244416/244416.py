def boards_equal(board1: list[list[bool]], board2: list[list[bool]]) -> bool:
    """
    Check if two Game of Life boards are exactly the same.

    Parameters:
        board1 (list[list[bool]]): The first Game of Life board.
        board2 (list[list[bool]]): The second Game of Life board.

    Returns:
        bool: True if the boards have the same dimensions and identical values 
              in every position, False otherwise.
    """

    if board1 == [] and board2 == []:
        return True

    if len(board1) == len(board2) and len(board1[0]) == len(board2[0]):
        for i in range(len(board1)):
            for j in range(len(board1[0])):
                if board1[i][j] != board2[i][j]:
                    return False
        
        return True

    else:
        return False

    
