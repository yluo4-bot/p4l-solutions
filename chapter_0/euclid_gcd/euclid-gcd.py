# Insert your euclid_gcd() function here.
def euclid_gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor (GCD) of two integers using Euclid's algorithm.
    Args:
        a: First integer.
        b: Second integer.
    Returns:
        The non-negative GCD of a and b.
    """
    a = abs(a)
    b = abs(b)

    if b == 0:
        return a 

    return euclid_gcd(b, a % b)
