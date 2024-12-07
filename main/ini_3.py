from helper import validator

def string_slicing(string: str, a: int, b: int, c: int, d: int) -> str:
    """
    This function The slice of this string from indices a through b and c through d (with space in between), inclusively.
    :param string: The string that will be sliced
    :param a: First index
    :param b: Second index
    :param c: Fourth index
    :param d: Fifth index
    :return:
        str: Sliced words
    """

    validator.validate_positive_number(a, b, c, d)
    validator.validate_second_number_is_greater(a, b)
    validator.validate_second_number_is_greater(c, d)
    first_word = string[a : b + 1]
    second_word = string[c : d + 1]
    return f"{first_word} {second_word}"


print(string_slicing("ADAaRHCeR3eYI0OWckZuwt86x7ARGrM8eEXSEY6gS5alJ8zCircusaRT4b7FtGPJqIFDbBON1FdXiWvG2THqJ2dV3nIjuu2sLkHy5RjiQhsansPWg4UgzOfHLyoX0Dg6fKytoLGw1DdOWu4q85ApUlT0VdoWhmUMzho8mcIEptkfuH3H8Qtm2YZYheliacaVIkdW2.", 47, 52, 184, 190))