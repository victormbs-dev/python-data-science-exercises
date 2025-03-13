

def calculate_moving_average(list_values=[], window_size=0):
    """
    Calculate the moving average of a list of values.
    Args:
        list_values (list of float): The list of numerical values to calculate
        the moving average for.
        window_size (int): The size of the moving window to calculate the
        average.
    Returns:
        list of float: A list containing the moving averages.
    """

    if not list_values:
        raise ValueError("The list of values cannot be empty.")

    if not all(isinstance(x, (int, float)) for x in list_values):
        raise TypeError("The list of values must contain only"
                        "numerical values.")

    if window_size <= 0 or window_size > len(list_values):
        raise ValueError("window_size must be greater than 0 and less than the"
                         "length of list_values.")

    result = []
    current_sum = sum(list_values[:window_size])
    result.append(current_sum / window_size)

    for i in range(window_size, len(list_values)):
        current_sum += list_values[i] - list_values[i - window_size]
        result.append(current_sum / window_size)

    return result


calculate_moving_average([10, 20, 30, 40, 50, 60, 70, 80], 5)
