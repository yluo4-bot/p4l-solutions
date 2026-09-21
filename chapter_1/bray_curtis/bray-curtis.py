import sys
# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.

# Insert your bray_curtis_distance() function here, along with any subroutines that you need.
def  bray_curtis_distance(sample1: dict[str, int], sample2: dict[str, int]) -> float:
    """
    Compute the Bray-Curtis distance between two frequency tables.

    Args:
        sample1: A frequency table mapping strings to integers.
        sample2: A frequency table mapping strings to integers.
    Returns:
        The Bray-Curtis distance between the two samples.
    """

    return float(1 - (sum_of_minima(sample1, sample2) / ((sum_of_values(sample1) + sum_of_values(sample2)) / 2)))
# Hint: you will probably need sum_of_minima() and sum_of_values() as subroutines.
    
# Note: for the sake of convenience, we are providing a min2() function below.

def sum_of_values(sample: dict) -> int:
    count = 0

    for points in sample.values():
        count += points

    return count

def sum_of_minima(sample1: dict, sample2: dict) -> int:
    minSum = 0

    for name1 in sample1: 
        if name1 in sample2:
            minSum += min2(sample1[name1], sample2[name1])


    return minSum

def min2(x: int, y: int) -> int:
    if x < y:
        return x
    return y
