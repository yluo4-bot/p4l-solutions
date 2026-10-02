# Recitation 4: Binary Search. Zero points.
#
# The list of strings is already sorted, and that is a lot of structure.
# Follow the rules from the slides: keep min_index and max_index, and look at
# mid = (min_index + max_index) // 2. If items[mid] comes before the pattern,
# the first copy must be to its right, so set min_index = mid + 1. Otherwise
# the first copy (if there is one) is at mid or to its left, so set
# max_index = mid. Stop when min_index and max_index are at most one apart,
# then check them.
#
# The list may contain repeated strings. Return the index of the FIRST copy.
# Python compares strings alphabetically with <, so "ACG" < "ACT" is True.

def first_occurrence(items: list[str], pattern: str) -> int:
    """
    Find the first index of a pattern in a sorted list using binary search.

    Parameters:
    - items (list[str]): Strings in ascending alphabetical order.
    - pattern (str): The string to look for.

    Returns:
    - int: The smallest index i with items[i] == pattern, or -1 if the
      pattern does not occur in items.
    """

    if len(items) == 0:
        return -1

    ran = (0, len(items) - 1)

    while ran[1] - ran[0] > 1:
        mid = (ran[0] + ran[1]) // 2 

        if items[mid] < pattern:
            ran = (mid + 1, ran[1])
        
        else:
            ran = (ran[0], mid)

    if items[ran[0]] == pattern:
        return ran[0]

    if items[ran[1]] == pattern:
        return ran[1]

    return -1
