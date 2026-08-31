# Insert your factorial() function here.
def factorial(n: int) -> int:
    """
    Compute n! (factorial) using a while loop.
    Args:
        n: A non-negative integer.
    Returns:
        The factorial of n.
    """
    a = 1

    while(n > 0):
        a *= n
        n -= 1

    return a
