# Insert your find_frequent_words() function here, along with any subroutines that you need.
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

def max_map_value(dict_values: dict) -> int:
    """
    max_map_value finds the maximum value of a given dictionary.

    Parameters:
    - dict_values (dict): A dictionary that has integers as values.

    Retursn:
    - int: The highest value key in the given dictionary.
    """
    nums = list(dict_values.values())

    maxVal = nums[0]

    for i in nums:
        if i > maxVal:
            maxVal = i

    return maxVal

def find_frequent_words(text: str, k: int) -> list[str]:
    """
    find_frequent_words returns a list containing the most frequent k-mers occurring in text,           including overlaps.
    Parameters:
    - text (str): A given text for the function.
    - k (int): The size of the k-mers.
    Returns:
    - The list of the most frequent k-mers occurring in text, including overlaps.
    """
    kmerList = []

    dictWords = frequency_table(text, k)
    maxValue = max_map_value(dictWords)
    
    for i in dictWords:
        if dictWords[i] == maxValue:
            kmerList.append(i)

    return kmerList
