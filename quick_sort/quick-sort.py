# Recitation 3: Sorting II. Zero points.
#
# Quicksort is the lazy way to sort. Pick one of the strings at random and
# call it the pivot. Put every string smaller than the pivot in one list and
# every string larger than the pivot in another. Now hand each of those two
# lists to someone else to sort (that is, call quick_sort on each of them),
# and glue the results back together: sorted smaller strings, then the
# pivot, then sorted larger strings.
#
# A list with zero or one strings is already sorted. That is your base case.
#
# Python compares strings alphabetically with <, so "ACG" < "ACT" is True.
# The input may contain repeated strings; every copy must appear in the output.

from random import choice

def quick_sort(items: list[str]) -> list[str]:
    """
    Sort a list of strings into alphabetical order using quicksort.

    Parameters:
    - items (list[str]): The strings to sort.

    Returns:
    - list[str]: A list containing the same strings in ascending
      alphabetical order. The original list is not changed.
    """

    if len(items) == 1:
        return items

    if len(items) == 0:
        return []

    pivot = choice(items)
    smaller = []
    equal = []
    larger = []

    for i in range(len(items)):
        if items[i] < pivot:
            smaller.append(items[i])

        elif items[i] > pivot:
            larger.append(items[i])

        else:
            equal.append(items[i])

    return quick_sort(smaller) + equal + quick_sort(larger)
