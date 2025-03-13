

import numpy as np


def normalized(values=[]):
    """Normalizes a list of lists of numerical values.
    Each internal list is normalized using the formula:
        normalized_value = (value - min_value) / (max_value - min_value)
    Args:
        values (list of list of numbers): List of lists containing the values
        to normalize.
    Returns:
        list of list of numbers: List of lists with normalized values.
    """

    if not values:
        raise ValueError("The list of values is empty")

    if not all(isinstance(i, list) for i in values):
        raise ValueError("The list of values must contain lists")

    if not all(isinstance(j, (int, float)) for i in values for j in i):
        raise ValueError("The list of values must contain only numbers")

    final = []

    for row in values:
        # Get the minimum and maximum values of the current list
        minim, maxim = min(row), max(row)

        # Normalize each value in the list using the formula
        if maxim == minim:
            final.append([0]*len(row))
        else:
            norm_array = [(x - minim)/(maxim - minim) for x in row]
            final.append(norm_array)

    return final


def standarized(values=[]):
    """Standardizes a list of lists of numerical values.
    Each internal list is standardized using the formula:
        standardized_value = (value - mean) / standard_deviation
    Args:
        values (list of list of numbers): List of lists containing the values
        to standardize.
    Returns:
        list of list of numbers: List of lists with standardized values.
    """
    if not values:
        raise ValueError("The list of values is empty")

    if not all(isinstance(i, list) for i in values):
        raise ValueError("The list of values must contain lists")

    if not all(isinstance(j, (int, float)) for i in values for j in i):
        raise ValueError("The list of values must contain only numbers")

    final = []
    for i in values:
        mean = np.mean(i)   # Mean of the current list
        std = np.std(i)     # Standard deviation of the current list

        # Standardize each value in the list using the formula and round to 1
        # decimal place
        standarized_array = [round(((j - mean) / std), 1) for j in i]
        final.append(standarized_array)
    return final


def transform_data(values=[]):
    """Transforms the data by applying normalization and standardization.
    This function applies the `normalized` and `standarized` functions to the
    same list of values and stores the results in a dictionary.
    Args:
        values (list of list of numbers): List of lists containing the values
        to transform.
    Prints:
        dict: Dictionary with two keys: 'normalized' and 'stan', each
        containing
        the corresponding normalized and standardized values.
    """
    if not values:
        raise ValueError("The list of values is empty")

    if not all(isinstance(i, list) for i in values):
        raise ValueError("The list of values must contain lists")

    if not all(isinstance(j, (int, float)) for i in values for j in i):
        raise ValueError("The list of values must contain only numbers")

    norm = normalized(values)   # Normalize the values
    stan = standarized(values)  # Standardize the values

    # Create the result dictionary
    result = dict(nomalizado=norm, estandarizado=stan)
    return result   # Return the result dictionary


# Execute the function with a test list
transform_data(
    [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
)
