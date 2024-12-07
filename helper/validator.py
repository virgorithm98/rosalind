def validate_positive_number(*numbers: int):
    """
    This function will check whether all numbers are positive numbers. Raise a ValueError if they are not.
    :param numbers: A collection of integers
    :return: None
    """
    for number in numbers:
        if number <= 0:
            raise ValueError("Parameter value cannot be negative")

def validate_second_number_is_greater(a: int, b: int):
    """
    This function will check whether b is greater than a. Raise a ValueError if it is not.
    :param a: First integer
    :param b: Second integer
    :return: None
    """
    if b < a:
        raise ValueError("First number is greater than the second number")