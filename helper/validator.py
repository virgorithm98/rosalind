def validate_positive_number(*numbers):
    for number in numbers:
        if number <= 0:
            raise ValueError("Parameter value cannot be negative")