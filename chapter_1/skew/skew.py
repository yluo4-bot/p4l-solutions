# Insert your skew() function here, along with any subroutines that you need.
def skew(symbol: str) -> int:
    """
    skew returns 1 or -1 if the given single character string is either
    G or C respectively, otherwise returns zero. (Throws error if the 
    given string does not have a length of one).

    Parameters:
    - symbol (str): A given one character string.

    Returns:
    - int: The symbol's respective skew score.
    """

    if len(symbol) != 1:
        raise ValueError("Length of string must be 1.")

    if symbol == "G":
        return 1
    
    if symbol == "C":
        return -1

    return 0
    
