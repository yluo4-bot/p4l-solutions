# Insert your factorial_array() function here, along with any subroutines that you need.
def factorial_array(n: int) -> list[int]:
    """
    Return a list of factorials from 0! through n!.
    Args:
        n: A non-negative integer.
    Returns:
        A list L of length n + 1 where L[k] == k! for k in [0, n].
    """
    L = []
    L.append(1)
    prior = L[0]
    for i in range(1, n + 1):
        num = i * prior
        L.append(num)
        prior = num
            
    return L
