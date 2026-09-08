# Write your pattern_count() function here, along with any subroutines that you need.
def starting_indices(pattern: str, text: str) -> list:
    """
    starting_indices returns the list containing all the starting positions of 
    pattern in text.

    Parameters:
    - pattern (str): A given substring.
    - text (str): A given superstring.

    Returns:
    - list: A list containing the starting positions of pattern in text (indices).
    """
    patternList = []

    for i in range(len(text) - len(pattern) + 1):
        if text[i : i + len(pattern)] == pattern:
            patternList.append(i)

    return patternList

def pattern_count(pattern: str, text: str) -> int:
    """
    pattern_count finds the number of occurences that a given substring occurs in
    a given text string. (Relies on starting_indices as a subroutine)

    Parameters:
    - pattern (str): The substring you search for in text.
    - text (str): The parent string you are using in your search.

    Returns:
    - int: The number of times that pattern occurs in text.
    """
    list1 = starting_indices(pattern, text)

    return len(list1)
