# Insert your cross_off_multiples() function here, along with any subroutines that you need.
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
    for i in range(0, len(prime_booleans)):
        if i % p == 0 and i > p:
            prime_booleans[i] = False


    return prime_booleans
