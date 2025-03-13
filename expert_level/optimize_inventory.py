# %%
def optimize_inventory(products, capacity):
    """
    Optimize the distribution of products across warehouses given a capacity
        constraint.
    This function takes a list of product sizes and a warehouse capacity, and
        distributes
    the products into the minimum number of warehouses such that the sum of
        the sizes of
    the products in each warehouse does not exceed the given capacity.
    Parameters:
    products (list of int): A list of integers representing the sizes of the
        products.
    capacity (int): The maximum capacity of each warehouse.
    Returns:
    list of list of int: A list of warehouses, each represented as a list of
        product sizes.
    Raises:
    ValueError: If the products list is empty.
    ValueError: If the capacity is not a positive integer.
    ValueError: If any element in the products list is not an integer.
    """

    if not products:
        raise ValueError("No products to optimize")

    if capacity <= 0 or not isinstance(capacity, int):
        raise ValueError("Invalid capacity")

    if not all(isinstance(product, int) for product in products):
        raise ValueError("products must be a list of integers")

    products.sort(reverse=True)

    warehouses = []

    for product in products:
        placed = False

        for warehouse in warehouses:
            if sum(warehouse) + product <= capacity:
                warehouse.append(product)
                placed = True
                break

        if not placed:
            warehouses.append([product])

    return warehouses


products = [5, 8, 3, 7, 2, 6, 4]
capacity = 10

optimize_inventory(products, capacity)
