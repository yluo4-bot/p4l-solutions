# Write your square_middle() function here along with any subroutines that you need.
def square_middle(x, num_digits):
    """
    Get the middle digits of x squared.

    Parameters:
    - x (int): a positive integer
    - num_digits (int): the number of digits in the middle of x squared to return

    Returns:
    int: the middle digits of x squared
    """

    if x < 0 or num_digits % 2 != 0 or num_digits <= 0 or count_num_digits(x) > num_digits:
        return -1

    xsq = x ** 2
    xsqStr = str(xsq)
    nd = count_num_digits(xsq)

    if nd < 2 * num_digits:
        xsqStr = "0" * (2 * num_digits - nd) + xsqStr

    start = num_digits // 2
    middle = xsqStr[start : start + num_digits]

    return int(middle)

def count_num_digits(x: int) -> int:
    x = str(x)
    d = len(x)

    if "-" in x:
        d = d - 1

    return d
