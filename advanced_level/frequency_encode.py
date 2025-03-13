from collections import Counter


def frequency_encode(values_list=[]):
    """
    Perform frequency encoding on a list of categorical variables.

    Args:
        category_list (list): A list of categorical values.

    Returns:
        list: A list of frequency-encoded values.
    """
    if not values_list:
        raise ValueError("The list of values is empty.")

    if not all(isinstance(value, str) for value in values_list):
        raise ValueError("The list contains non-string values.")

    counts = Counter(values_list)
    list_length = len(values_list)

    # Calculate the frequency relative to the total count
    frequencies = {key: value / list_length for key, value in counts.items()}

    # Replace each category in the list with its frequency
    encoded_list = [round(frequencies[item], 2) for item in values_list]

    return encoded_list


frequency_encode(["rojo", "azul", "rojo", "verde", "azul", "azul"])
