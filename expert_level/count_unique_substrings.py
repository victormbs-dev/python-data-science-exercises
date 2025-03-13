

def count_unique_substrings(text, n):
    """
    Count the occurrences of all unique substrings of length n in the given
        text.
    Parameters:
    text (str): The input string in which to count substrings.
    n (int): The length of the substrings to count.
    Returns:
    dict: A dictionary where the keys are unique substrings of length n and
        the values are their respective counts.
    Raises:
    ValueError: If n is not a positive integer less than or equal to the
        length of the text.
    """

    if n > len(text) or n <= 0:
        raise ValueError("n must be a positive integer less than or equal to"
                         "the length of the text")

    substring_counts = {}

    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        substring_counts[substring] = substring_counts.get(substring, 0) + 1

    return substring_counts


print(count_unique_substrings("banana", 3))
