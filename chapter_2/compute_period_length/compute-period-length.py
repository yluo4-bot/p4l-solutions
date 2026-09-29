# Write your compute_period_length() function here along with any subroutines that you need
def compute_period_length(a: list[int]) -> int:
    """
    Compute the period length of a list of integers.

    Parameters:
    - a: a list of integers

    Returns:
    int: the length of the period of a
    """

    if has_repeat(a) == 0:
        return 0

    dictNum = {}

    for i in a:

        if i in dictNum:
            dictNum[i] += 1

        else:
            dictNum[i] = 1

    maxNum = 0
    maxInt = ""

    for i in dictNum:
        if dictNum[i] > maxNum:
            maxNum = dictNum[i]
            maxInt = i

    i1 = 0
    i2 = 0

    i1 = a.index(maxInt)
    i2 = a[i1 + 1 : len(a)].index(maxInt) + i1 + 1

    return i2 - i1


def has_repeat(a: list[int]) -> bool:
    dictNum = {}

    for i in a:

        if i in dictNum:
            dictNum[i] += 1

        else:
            dictNum[i] = 1

    for i in dictNum:
        
        if dictNum[i] > 1:
            return True

    return False
