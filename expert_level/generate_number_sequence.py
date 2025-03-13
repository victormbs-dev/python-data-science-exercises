def generate_number_sequence(type="incremento", size=5, init_value=1):
    """
    Generates a sequence of numbers based on the specified type.
    Parameters:
    type (str): The type of sequence to generate. Options are:
                - "incremento": Generates an increasing sequence.
                - "decremento": Generates a decreasing sequence.
                - "alternante": Generates an alternating sequence.
    size (int): The number of elements in the sequence. Must be a non-negative
        integer.
    init_value (int): The starting value of the sequence. Must be a
    non-negative integer.
    Returns:
    list: A list containing the generated sequence of numbers, or None if
    invalid parameters are provided.
    """

    if type not in ["incremento", "decremento", "alternante"]:
        print("Invalid type")
        return None

    if not isinstance(size, int) or size < 0:
        print("Invalid size")
        return None

    if not isinstance(init_value, int) or init_value < 0:
        print("Invalid init_value")
        return None

    if type == "incremento":
        final_list = [init_value + i for i in range(size)]
    elif type == "decremento":
        final_list = [init_value - i for i in range(size)]
    elif type == "alternante":
        final_list = [init_value + i if i % 2 == 0 else -abs(init_value + i)
                      for i in range(size)]
    else:
        print("Invalid type")
        return None
    return final_list


generate_number_sequence(type="alternante", size=5, init_value=1)
