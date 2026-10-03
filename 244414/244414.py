import random

def dice_outcome_matrix(trials: int, seed: int) -> list[list[int]]:
    """
    Simulate rolling two fair six-sided dice `trials` times and return a 6×6 matrix
    of counts. Entry [i][j] is the number of times die1 showed (i+1) and die2 showed (j+1).

    Parameters:
        trials (int): The number of dice rolls to simulate (≥ 1).
        seed (int): random seed for reproducibility.

    Returns:
        list[list[int]]: A 6×6 matrix of counts.
    """

    matr = [[0] * 6 for _ in range(6)]
    random.seed(seed)

    for i in range(trials):
        d1 = rollDice()
        d2 = rollDice()
        matr[d1 - 1][d2 - 1] += 1


    return matr

def rollDice() -> int:
    return int(random.randint(1, 6))
