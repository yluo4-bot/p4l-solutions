# Please do not remove imports; the autograder relies on standard I/O behavior.
import sys

from math import isqrt

def find_even_divisors(n: int) -> list[int]:
    """
    Return all even positive divisors of n as a list of ints, in any order
    (your tests can enforce ordering if desired).

    Parameters
    ----------
    n : int
        The integer whose even divisors to compute.

    Returns
    -------
    list[int]
        A list of even positive divisors of n.

    Raises
    ------
    ValueError
        If n is not an int (note: bool is not allowed).
    """
    # Parameter checks
    if isinstance(n, bool) or not isinstance(n, int):
        raise ValueError("n must be an integer")

    # your code here

    evenPositiveDivisorList = []

    for i in range(2, n + 1, 2):
        if n % i == 0:
            evenPositiveDivisorList.append(i)

    return evenPositiveDivisorList
