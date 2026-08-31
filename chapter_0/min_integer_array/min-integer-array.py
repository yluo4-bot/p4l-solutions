def min_integer_array(lst: list[int]) -> int:
    """
    Return the minimum integer in a non-empty list.
    Args:
        lst: A non-empty list of integers.
    Returns:
        The smallest integer in lst.
    Raises:
        ValueError: If lst is empty.
    """
    minimum = lst[0]
    for i in lst:
        if(i < minimum):
            minimum = i

    return minimum
