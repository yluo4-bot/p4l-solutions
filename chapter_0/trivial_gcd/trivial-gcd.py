def trivial_gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor (GCD) of two integers using the "trivial" (brute-force) algorithm.
    Args:
        a: First integer.
        b: Second integer.
    Returns:
        The non-negative GCD of a and b. 
    """
    a = abs(a)
    b = abs(b)

    ran = b
    if a > b:
        ran = a
    maxGCD = 0
    if a == 0 and b == 0:
        return maxGCD

    for i in range(1, ran + 1):
        if a % i == 0 and b % i == 0:
            maxGCD = i

    return maxGCD

# Place your min_2() subroutine here.
