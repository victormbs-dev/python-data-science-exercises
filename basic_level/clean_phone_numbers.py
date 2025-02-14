

import re


def clean_phone_numbers(numbers=[]):

    """
    Cleans and validates a list of phone numbers by removing formatting
        characters
    and ensuring they are valid 10-digit numbers.

    Parameters:
        numbers (list): A list of strings representing phone numbers in
            various formats.

    Returns:
        list: A list of cleaned phone numbers as 10-digit strings.
    """

    if not numbers:
        raise ValueError("No phone numbers found.")

    valid_numbers = []
    invalid_numbers = []

    for number in numbers:

        number_cleaned = re.sub(r"[^\d]", "", number)

        if len(number_cleaned) > 10:
            number_cleaned = number_cleaned[-10:]

        if len(number_cleaned) == 10 and number_cleaned.isdigit():
            valid_numbers.append(number_cleaned)
        else:
            invalid_numbers.append(number)

    return dict(valid=valid_numbers, invalid=invalid_numbers)


clean_phone_numbers(["+1 (555) 123-4567", "555-123-4567", "1234567890",
                     "+52 55 1234 5678", "Hello, World!"])
