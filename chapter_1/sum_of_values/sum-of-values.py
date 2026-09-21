import sys
# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.

# Insert your sum_of_values() function here.
def sum_of_values(sample: dict) -> int:
    """
    sum_of_values finds the sum of all the integer values in the 
    key of the dictionary.

    Parameters:
    - sample1 (dict): The sample or frequency table.

    Returns:
    - int: The sum of the keys in the given sample1.
    """

    count = 0

    for freq in sample.values():
        count += freq

    return count
