import numpy as np


def remove_outliers(list_numbers=[]):
    """
    Removes outliers from a list of numbers using the Interquartile Range (IQR)
    method.
    Parameters:
    list_numbers (list): A list of numeric values (integers or floats).
    Returns:
    dict: A dictionary with two keys:
        - 'cleaned_list': A list of numbers with outliers removed.
        - 'removed_values': A list of the outliers that were removed.
    Raises:
    ValueError: If the input list is empty or contains non-numeric values.
    """
    if len(list_numbers) < 2:
        raise ValueError("The list is empty")

    if not all(isinstance(i, (int, float)) for i in list_numbers):
        raise ValueError("The list contains non-numeric values")

    Q1 = np.percentile(list_numbers, 25)
    Q3 = np.percentile(list_numbers, 75)

    range_IQR = Q3 - Q1
    limits_Q1 = Q1 - 1.5 * range_IQR
    limits_Q3 = Q3 + 1.5 * range_IQR

    final_list = [i for i in list_numbers if i >= limits_Q1 and i <= limits_Q3]
    numbers_removed = [i for i in list_numbers if i < limits_Q1 or i >
                       limits_Q3]

    return dict(cleaned_list=final_list, removed_values=numbers_removed)


remove_outliers([10, 12, 14, 15, 18, 22, 23, 30, 100])
