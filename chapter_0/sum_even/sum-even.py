# Insert your sum_even() function here.
def sum_even(k: int) -> int:
    """
    Return the sum of all positive even integers up to and including k.
    Args:
        k: Upper bound (integer). Only positive even numbers ≤ k are summed.
    Returns:
        The sum 2 + 4 + ... + (largest even ≤ k). Returns 0 if k < 2.
    """
    total = 0

    for i in range(0, k + 1, 2):
        total += i
    return total
