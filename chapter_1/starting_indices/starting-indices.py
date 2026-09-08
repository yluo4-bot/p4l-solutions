 

# Insert your starting_indices() function here.
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
