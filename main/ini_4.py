from helper.validator import validate_positive_number


def sum_all_odd_in_between(a: int, b: int) -> int:
    """
    This function will return the sum of all odd numbers between a and b inclusively
    :param a: Start
    :param b: End
    :return: Sum of all odd numbers between a and b inclusively
    """

    validate_positive_number(a, b)

    return sum(i for i in range(a, b + 1) if i % 2 != 0)

print(sum_all_odd_in_between(4457, 9095))
