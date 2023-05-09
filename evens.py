def even_number_of_evens(numbers):
    """
    Should raise TypeError if a list is not passed into the function
    error message: "A list was not passed into the function"
    if numbers is empty return False
    if the number of evens is odd, return False
    if the number of evens is 0, return False
    if the number of evens is even, return True
    """
    if isinstance(numbers, list):
        evens = 0

        for n in numbers:
            if n % 2 == 0:
                evens += 1

        if evens:
            return evens % 2 == 0
        else:
            return False
    else:
        raise TypeError("A list wass not passed into the function")


if __name__ == '__main__':
    print(even_number_of_evens(5))
