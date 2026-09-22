import sys

# Please do not remove imports because these are used by the autograder.
# If you need additional imports, then you may declare them above.


def find_flanking_regions(text: str, pattern1: str, pattern2: str) -> list[str]:
    """
    Find all substrings of `text` that are flanked by `pattern1` on the left
    and `pattern2` on the right.

    Parameters
    ----------
    text : str
        The input string to search.
    pattern1 : str
        The left flanking pattern.
    pattern2 : str
        The right flanking pattern.

    Returns
    -------
    list[str]
        A list of substrings between pattern1 and pattern2. Can be empty if none found.
    """

    # your code goes here

    listFlReg = []

    p1 = len(pattern1)
    p2 = len(pattern2)
    t = len(text)

    for i in range(t):
        if i + p1 <= t and text[i : i + p1] == pattern1:
            for j in range(i + p1 - 1, t):
                if j + p2 <= t and text[j: j + p2] == pattern2:
                    listFlReg.append(text[i : j + p2])

    return listFlReg
