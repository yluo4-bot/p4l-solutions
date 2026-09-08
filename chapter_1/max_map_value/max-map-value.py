 

# Insert your max_map_value() function here.
def max_map_value(dict_values: dict) -> int:
    """
    max_map_value finds the maximum value of a given dictionary.

    Parameters:
    - dict_values (dict): A dictionary that has integers as values.

    Retursn:
    - int: The highest value key in the given dictionary.
    """
    nums = list(dict_values.values())

    maxVal = nums[0]

    for i in nums:
        if i > maxVal:
            maxVal = i

    return maxVal
