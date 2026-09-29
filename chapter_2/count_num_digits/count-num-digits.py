# Write your count_num_digits() function here along with any subroutines that you need.
def count_num_digits(x: int) -> int:
    """
    Count the number of digits in a positive integer x.

    Parameters:
    - x (int): a positive integer

    Returns:
    int: the number of digits in x
    """

    x = str(x)
    d = len(x)

    if "-" in x:
        d = d - 1

    return d
