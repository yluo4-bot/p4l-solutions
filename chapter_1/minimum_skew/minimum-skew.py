# Insert your minimum_skew() function here, along with any subroutines that you need.
def skew(symbol: str) -> int:
    if len(symbol) != 1:
        raise ValueError("Length of string must be 1.")

    if symbol == "G":
        return 1
    
    if symbol == "C":
        return -1

    return 0

def skew_array(genome: str) -> list[int]:

    listSkew = [0] * (len(genome) + 1)

    for i in range(1, len(genome) + 1):
        listSkew[i] = listSkew[i - 1] + skew(genome[i - 1])
    
    return listSkew

def minimum_skew(genome: str) -> list[int]:
    """
    minimum_skew finds the list of integers representing all integer indices that minimizes the skew     of the genome text.
    Parameters:
    - genome (str): A genome string.
    Returns:
    - list[int]: A list of indices that minimize the skew value of the genome text.
    """

    listSkew = skew_array(genome)
    listMinSkew = []

    minimumVal = listSkew[0]

    for i in range(len(listSkew)):
        if listSkew[i] < minimumVal:
            minimumVal = listSkew[i]

    for i in range(len(listSkew)):
        if listSkew[i] == minimumVal:
            listMinSkew.append(i)

    return listMinSkew
