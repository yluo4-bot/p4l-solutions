# Insert your skew_array() function here, along with any subroutines that you need.
def skew(symbol: str) -> int:
    if len(symbol) != 1:
        raise ValueError("Length of string must be 1.")

    if symbol == "G":
        return 1
    
    if symbol == "C":
        return -1

    return 0

def skew_array(genome: str) -> list[int]:
    """
    skew_array returns the list that represents the skew at each position of the genome. That is,       the i-th position in the list is the skew at the i-th position of the genome.
    Parameters:
    - genome (str): A genome string.
    Returns:
    - list[int]: A list representing the skew of the genome string.
    """

    listSkew = [0] * (len(genome) + 1)

    for i in range(1, len(genome) + 1):
        listSkew[i] = listSkew[i - 1] + skew(genome[i - 1])
    
    return listSkew
    
