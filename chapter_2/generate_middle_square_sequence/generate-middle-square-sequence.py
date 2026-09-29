# Write your generate_middle_square_sequence() function here along with any subroutines that you need.
def generate_middle_square_sequence(seed: int, num_digits: int) -> list[int]:
    """
    Generate a middle square sequence.

    Parameters:
    - seed (int): the first value in the sequence
    - num_digits (int): the number of digits in the middle of each squared value to add to the sequence

    Returns:
    list: a middle-square sequence
    """

    seq = [seed]

    while has_repeat(seq) == False:
        seed = square_middle(seed, num_digits)
        seq.append(seed)

    return seq

def square_middle(x, num_digits):
    if x < 0 or num_digits % 2 != 0 or num_digits <= 0 or count_num_digits(x) > num_digits:
        return -1

    xsq = x ** 2
    xsqStr = str(xsq)
    nd = count_num_digits(xsq)

    if nd < 2 * num_digits:
        xsqStr = "0" * (2 * num_digits - nd) + xsqStr

    start = num_digits // 2
    middle = xsqStr[start : start + num_digits]

    return int(middle)

def count_num_digits(x: int) -> int:
    x = str(x)
    d = len(x)

    if "-" in x:
        d = d - 1

    return d

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
