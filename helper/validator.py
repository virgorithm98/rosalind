def validate_positive_number(*numbers: int):
    for number in numbers:
        if number <= 0:
            raise ValueError("Parameter value cannot be negative")

def validate_second_number_is_greater(a: int, b: int):
    if b < a:
        raise ValueError("First number is greater than the second number")