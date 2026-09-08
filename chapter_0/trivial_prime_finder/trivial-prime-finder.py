# Provided for you (from an earlier exercise):
def is_prime(p: int) -> bool:
    """
    Determine whether an integer is prime.
    Args:
        p: Integer to test (may be negative or zero).
    Returns:
        True if p is prime, False otherwise.
    """
    if p == 1 or p == 0:
        return False  # base case: p is not prime

    # iterate over potential divisors up to the square root of p
    for k in range(2, int(p ** 0.5 + 1)):
        if p % k == 0:
            return False  # k is a divisor of p, so p is not prime

    # if no divisors are found, p is prime
    return True


# Insert your trivial_prime_finder() function here, along with any subroutines that you need.
def trivial_prime_finder(n: int) -> list[bool]:
    """
    Returns a list of boolean variables storing the primality of each nonnegative integer up to and including n.
    Parameters:
    - n (int): an integer
    Returns:
    list (bool): a list of boolean variables storing the primality of each nonnegative integer up to and including n.
    """
    listPrime = []

    for i in range(0, n + 1):
        listPrime.append(is_prime(i))

    return listPrime

# Hint: place your is_prime() subroutine here.
