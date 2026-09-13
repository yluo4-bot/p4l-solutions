# Insert your find_clumps() function here, along with any subroutines that you need.
def frequency_table(text: str, k: int) -> dict:
    """
    frequency_table finds the frequencies of each k-mer occuring in a given text, 
    including overlaps.

    Parameters:
    - text (str): The string text to search for kmers.
    - k (int): The size of the kmers.

    Returns:
    - dict (str : int): The dictionary of kmers to their frequencies in the given
    text string, including overlaps.
    """

    counts = {}

    for i in range(len(text) - k + 1):
        kmer = text[i: i + k]
        if kmer in counts:
            counts[kmer] += 1
        else:
            counts[kmer] = 1

    return counts

def find_clumps(text: str, k: int, window_length: int, t: int) -> list[str]:
    """
    Finds a list of strings representing all k-mers that appear at least t times in a window of         given length in the string.
    Parameters:
    - text (str): An input string.
    - k (int): k-mer's of size k.
    - window_length (int): the size of substrings of text in which we are looking for clumps
    - t (int): The k-mers must appear at least t amount of times.
    Output:
    - list: A list of k-mers that occur at least t times in a window of length window_length in
    text.
    """


    patterns = []
    n = len(text)

    for i in range(n - window_length + 1):
        window = text[i: i + window_length]
        freqMap = frequency_table(window, k)
       
        for s in freqMap:
            if freqMap[s] >= t and s not in patterns:
                patterns.append(s)
    
    return patterns
    
