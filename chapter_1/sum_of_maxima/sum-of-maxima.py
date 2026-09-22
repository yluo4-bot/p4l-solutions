import sys
# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.


# Insert your sum_of_maxima() function here.
def sum_of_maxima(sample1: dict, sample2: dict) -> int:
    """
    sum_of_maxima returns the sum of the maxima of the values for shared keys
    across two samples. If a key is not shared it is still added to the sum.

    Parameters:
    - sample1 (dict): A given input sample.
    - sample2 (dict): Another given input sample.

    Returns:
    - int: The sum of the minima of all values for shared keys.  
    If a key is not shared it is still added to the sum.
    """
    maxSum = 0

    for name1 in sample1: 
        if name1 in sample2: 
            maxSum += max2(sample1[name1], sample2[name1])

        else: 
            maxSum += sample1[name1]

    for name2 in sample2:
        if name2 not in sample1: 
            maxSum += sample2[name2]

    return maxSum  

# Note: for the sake of convenience, we are providing a max2() function below.
def max2(x:int, y:int) -> int:
    """
    max_2 returns whatever value is larger, x or y, or the arguments to the function.

    Parameters:
    - x (int): A given integer.
    - y (int): A second integer.

    Returns:
    - int: The larger of the two, x or y.
    """
    if x > y:
        return x
    return y
