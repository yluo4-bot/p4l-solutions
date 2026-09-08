# Write your reverse_complement() function here, along with any subroutines that you need.
def reverse_complement(dna: str) -> str:
    """
    Compute the reverse complement of a DNA string.

    Args:
        dna: A DNA string.
    Returns:
        The reverse complement of the DNA string.
    """
    revCompStr = ""

    for i in range(len(dna)):
        compNuc = ""
        if dna[i] == "A" or dna[i] == "T":
            compNuc = chr(149 - ord(dna[i]))
        else:
            compNuc = chr(138 - ord(dna[i]))
        revCompStr =  compNuc + revCompStr

    return revCompStr
