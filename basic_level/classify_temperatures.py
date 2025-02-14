

def classify_temperatures(temperatures):

    """
    Converts a list of temperatures from Fahrenheit to Celsius and classifies
    each temperature
    into a category based on its Celsius value.

    Parameters:
        temperatures (list): A list of numeric values representing
        temperatures in Fahrenheit.

    Returns:
        dict: A dictionary containing:
            - 'F': The original temperature in Fahrenheit.
            - 'Celsius': The converted temperature in Celsius (rounded to one
                decimal place).
            - 'Category': The classification of the temperature as one of
                'High', 'Middle', or 'Low'.
    """

    if not temperatures:
        raise TypeError("The list cannot be empty.")

    if not isinstance(temperatures, list):
        raise ValueError("The input must be a list of numeric values.")

    if not all(isinstance(tem, (int, float)) for tem in temperatures):
        raise ValueError("""All elements in the list must be numbers
                         (int or float).""")

    final_list = []

    for t in temperatures:
        convertion = round((t - 32) * 5/9, 1)
        category = ''

        if convertion > 25:
            category = 'Hight'
        elif convertion >= 15:
            category = 'Middle'
        else:
            category = 'Low'

        result = dict(F=t, Celsius=convertion, Category=category)
        final_list.append(result)

    return final_list


classify_temperatures([32, 68, "Hola", 104])
