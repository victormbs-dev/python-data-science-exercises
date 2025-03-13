from collections import defaultdict

data = [
    {"nombre": "Juan", "edad": 28, "ciudad": "Ciudad A"},
    {"nombre": "Ana", "edad": 22, "ciudad": "Ciudad B"},
    {"nombre": "Luis", "edad": 30, "ciudad": "Ciudad A"},
    {"nombre": "Sara", "edad": 28, "ciudad": "Ciudad B"},
    {"nombre": "Marta", "edad": 28, "ciudad": "Ciudad A"},
]


def filter_and_group(info=[], filter_key='edad', value='28',
                     group_by='ciudad'):
    """Filters a list of dictionaries based on a specific key-value pair and
    groups the results by another key.

    Args:
        info (list of dict): List of dictionaries containing the data to be
        filtered and grouped.
        filter_key (str): The key used to filter the dictionaries.
        value (any): The value to filter the dictionaries by.
        group_by (str): The key used to group the filtered results.

    Returns:
        dict: A dictionary where keys are unique values from the `group_by`
        key and values are the counts of records in each group.
    """

    if not info:
        raise ValueError("The 'info' parameter must be a non-empty list of"
                         "dictionaries.")

    if not filter_key:
        raise ValueError("The 'filter_key' parameter must be a non-empty"
                         "string.")

    if not value:
        raise ValueError("The 'value' parameter must be a non-empty value.")

    if not group_by:
        raise ValueError("The 'group_by' parameter must be a non-empty"
                         "string.")

    # Filter records by the specified key-value pair
    filtered = [i for i in info if i.get(filter_key) == value]

    # Initialize a default dictionary to count occurrences by group
    grouped_count = defaultdict(int)

    for i in filtered:
        # Get the value of the grouping key
        group_value = i.get(group_by, None)
        # Ensure the grouping key exists in the record
        if group_value is not None:
            grouped_count[group_value] += 1
        else:
            # Print a warning if the grouping key is missing
            print(f"Key no found '{group_by}' in: {i}")

    # Convert the defaultdict to a regular dictionary
    return dict(grouped_count)


# Execute the function with a test list
filter_and_group(data, "edad", 28, "ciudad")

# Output esperado: {"Ciudad A": 2, "Ciudad B": 1}
