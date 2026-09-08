# Insert your is_prime() function here, along with any subroutines that you need.
from math import sqrt
def is_prime(p: int) -> bool:
    """
    Determine whether an integer is prime.
    Args:
        p: Integer to test (may be negative or zero).
    Returns:
        True if p is prime, False otherwise.
    """

    if p == 1:
        return False

    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False

    return True
