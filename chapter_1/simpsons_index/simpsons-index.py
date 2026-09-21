import sys
# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.

# Insert your simpsons_index() function here, along with any subroutines that you need.
def simpsons_index(sample: dict[str, int]) -> float:
    """
    Compute Simpson's index of a frequency table.

    Args:
        sample: A frequency table mapping strings to integers.
    Returns:
        The Simpson's index of the sample.
    """

    total = sum_of_values(sample)

    if total == 0:
        return 0.0

    index = 0.0

    for count in sample.values():

        p = count / total
        index += p * p

    return index
