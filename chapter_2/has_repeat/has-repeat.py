# Write your has_repeat() function here along with any subroutines that you need
def has_repeat(a: list[int]) -> bool:
    """
    Check if a list has repeat elements.

    Parameters:
    - a: a list of integers

    Returns:
    bool: True if a has repeat elements, False otherwise
    """
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
