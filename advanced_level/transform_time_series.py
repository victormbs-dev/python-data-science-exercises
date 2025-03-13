import numpy as np


def transform_time_series(list_values=[], window_size=0):
    """
    Transforms a list of numerical values into a list of dictionaries
    containing statistical metrics
    (mean, sum, and standard deviation) for each sliding window of the
    specified size.
    Parameters:
    list_values (list): A list of numerical values (integers or floats).
    window_size (int): The size of the sliding window.
    Returns:
    list: A list of dictionaries, each containing the following keys:
        - "media": The mean of the values in the current window, rounded to
        one decimal place.
        - "suma": The sum of the values in the current window.
        - "deviacion": The standard deviation of the values in the current
        window, rounded to one decimal place.
    Raises:
    ValueError: If window_size is less than or equal to 0, greater than the
    length of list_values,
                if list_values is empty, or if list_values contains
                non-numerical values.
    """

    if window_size <= 0 or window_size > len(list_values):
        raise ValueError("window_size cannot be 0 or greater than the length"
                         "of the list_values")

    if len(list_values) == 0:
        raise ValueError("list_values cannot be empty")

    if not all(isinstance(x, (int, float)) for x in list_values):
        raise ValueError("list_values must contain only integers or floats")

    sublist = [{
        "media": round(np.mean(list_values[i:i+window_size]), 1),
        "suma": np.sum(list_values[i:i+window_size]),
        "deviacion": round(np.std(list_values[i:i+window_size]), 1)}
        for i in range(len(list_values)-(window_size-1))]
    return sublist


transform_time_series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)