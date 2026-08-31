# Insert your sum_first_n_integers() function here.
def sum_first_n_integers(n: int) -> int:
    """
    Return the sum of the first n positive integers using a while loop.
    Args:
        n: The number of initial positive integers to sum (must be non-negative).
    Returns:
        The sum 1 + 2 + ... + n. Returns 0 if n == 0.
    Raises:
        ValueError: If n is negative.
    """
    total = 0

    while(n >= 0):
        total += n
        n -= 1

    return total
