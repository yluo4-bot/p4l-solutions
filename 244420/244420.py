def state_histogram(board: list[list[int]]) -> list[int]:
    """
    Compute a histogram of state frequencies in a board.

    Input:
        board (list[list[int]]): A rectangular board of integer states.

    Output:
        list[int]: A histogram list where hist[s] is the count of cells in state s,
                   for s = 0..max_state(board).
    """

    freq = [0] * (max_state(board) + 1) 

    for r in range(0, len(board)):
        for c in range(0, len(board[0])):
                freq[board[r][c]] += 1

    return freq


def max_state(board: list[list[int]]) -> int:

    m = board[0][0]

    for r in range(0, len(board)):
        for c in range(0, len(board[0])):
            if board[r][c] > m:
                m = board[r][c]

    return m
 
