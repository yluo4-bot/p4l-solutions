import sys
# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.

# Insert your jaccard_distance() function here, along with any subroutines that you need.
def jaccard_distance(sample1: dict[str, int], sample2: dict[str, int]) -> float:
    """
    Compute the Jaccard distance between two frequency tables.

    Args:
        sample1: A frequency table mapping strings to integers.
        sample2: A frequency table mapping strings to integers.
    Returns:
        The Jaccard distance between the two samples.
    """

    sumMax = sum_of_maxima(sample1, sample2)
    sumMin = sum_of_minima(sample1, sample2)

    return 1 - sumMin/sumMax

def sum_of_maxima(sample1: dict, sample2: dict) -> int:
    minSum = 0

    for name1 in sample1: 
        if name1 in sample2:
            minSum += min2(sample1[name1], sample2[name1])


    return minSum
    
# Note: for the sake of convenience, we are providing min2() and max2() functions below.
def min2(x: int, y: int) -> int:
    """
    Return the minimum of two integers.

    Args:
        x: An integer.
        y: An integer.
    Returns:
        The smaller of x and y.
    """
    if x < y:
        return x
    return y

def max2(x: int, y: int) -> int:
    """
    Return the maximum of two integers.

    Args:
        x: An integer.
        y: An integer.
    Returns:
        The larger of x and y.
    """
    if x > y:
        return x
    return y
