# Insert your permutation() function here, along with any subroutines that you need.
def permutation(n: int, k: int) -> int:
    """
    Compute the permutation statistic P(n, k) = n · (n-1) · ... · (n-k+1) = n! / (n-k)!.
    Args:
        n: Total number of distinct objects (non-negative).
        k: Number of positions to fill (non-negative).
    Returns:
        The number of ways to choose and order k items from n, i.e., P(n, k).
    """

    if k > n:
        return 0

    if k == 0:
        return 1

    result = 1

    for i in range(k):
        result *= n - i
    
    return result
