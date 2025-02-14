import re


def count_keyword_frequency(phrases=None, key_words=None):
    """
    Counts the frequency of specified keywords in a list of phrases using
    regex for precise word matching.

    Parameters:
        phrases (list): A list of strings, where each string is a phrase to
        analyze.
        key_words (list): A list of keywords (strings) to count in the phrases.

    Returns:
        list: A list of dictionaries, where each dictionary corresponds to a
              phrase and contains the frequency of each keyword.
    """
    if not phrases:
        raise ValueError("No phrases found")

    if not key_words:
        raise ValueError("No key_words found")

    if not all(isinstance(phrase, str) for phrase in phrases):
        raise TypeError("All phrases must be strings")

    if not all(isinstance(key_word, str) for key_word in key_words):
        raise TypeError("All key_words must be strings")

    result = []

    for phrase in phrases:
        frequency = {}
        lower_phrase = phrase.lower()

        for keyword in key_words:
            pattern = r'\b' + re.escape(keyword.lower()) + r'\b'
            matches = re.findall(pattern, lower_phrase)
            frequency[keyword] = len(matches)

        result.append(frequency)

    return result


phrases = [
    "el producto es bueno y bonito",
    "bueno y malo a la vez",
    "excelente servicio",
    "bueno, bueno y más bueno"
]

key_words = [
    "bueno",
    "malo",
    "excelente"
]

print(count_keyword_frequency(phrases, key_words))