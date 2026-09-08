# Provided for you (from an earlier exercise):
def cross_off_multiples(prime_booleans: list[bool], p:int) -> list[bool]:
    """
    Returns an updated list in which all variables in the array whose indices are multiples of p (greater than p) have
    been set to false.
    Parameters:
    - prime_booleans (list): a list of boolean variables storing the primality of each nonnegative integer
    - p (int): an integer
    Returns:
    list (bool): a list of boolean variables storing the primality of each nonnegative integer up to and including n with
    multiples of p (greater than p) set to false.
    """
    n = len(prime_booleans) - 1
    for k in range(2 * p, n + 1, p):
        prime_booleans[k] = False  # k is composite


# Insert your sieve_of_eratosthenes() function here, along with any subroutines that you need.
def sieve_of_eratosthenes(n: int) -> list[bool]:
    """
    Returns a list of boolean variables storing the primality of each nonnegative integer up to and including n,
    implementing the "sieve of Eratosthenes" algorithm.
    Parameters:
    - n (int): an integer
    Returns:
    list (bool): a list of boolean variables storing the primality of each nonnegative integer up to and including n.
    """
    listPrime = [True] * (n + 1)

    listPrime[0], listPrime[1] = False, False 

    for i in range(2, n + 1):
        if listPrime[i] == True:
            cross_off_multiples(listPrime, i)

    return listPrime

# Hint: insert your cross_off_multiples() function here
