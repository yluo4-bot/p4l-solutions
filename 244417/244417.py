def change_mask(board: list[list[bool]]) -> list[list[bool]]:
    """
    Given a Game of Life board, return a mask grid of the same size whose entries
    are True exactly at cells that will change state in the next generation.
    Args:
        board (GameBoard = list[list[bool]] ): A rectangular Game of Life board.

    Returns:
        list[list[bool]]: A grid of the same dimensions, where mask[r][c] is True
                          if and only if update_cell(board, r, c) != board[r][c].
    """

    mask = [[False] * len(board[0]) for _ in range(len(board))]

    for r in range(len(board)):
        for c in range(len(board[0])):
            if update_cell(board, r, c) != board[r][c]:
                mask[r][c] = True

    return mask
