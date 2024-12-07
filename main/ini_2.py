from helper import validator

def calculate_hypotenuse(a: int, b: int) -> int:
    validator.validate_positive_number(a, b)

    return a**2 + b**2

print(calculate_hypotenuse(913, 970))