# Write your reverse() function here.
def reverse(s: str) -> str:
    """
    reverse returns the given string backwards.

    Parameters:
    - s (str): The given string to reverse.

    Returns:
    - str: The reverse of s.
    """
    reversedString = ""
    for i in range(len(s) - 1, -1, -1):
        reversedString += s[i]

    return reversedString
