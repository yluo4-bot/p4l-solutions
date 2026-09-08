# Insert your complement() function here.
def complement(dna: str) -> str:
    """
    Finds the complementary strand of the given string.

    Parameters:
    - dna (str): A dna string.

    Returns:
    - str: the string whose i-th symbol is the complementary 
    nucleotide of the i-th symbol of the input string. (A-T, C-G, T-A, G-C).
    """
    compStr = ""

    for i in range(len(dna)):
        compNuc = ""
        if dna[i] == "A" or dna[i] == "T":
            compNuc = chr(149 - ord(dna[i]))
        else:
            compNuc = chr(138 - ord(dna[i]))
        compStr += compNuc

    return compStr
