import pytest, logging

from main.ini_2 import calculate_hypotenuse


def test_calculate_hypotenuse():
    logger = logging.getLogger("maiiiiin.py")
    logger.setLevel(logging.ERROR)
    logger.error("TEST")
    assert calculate_hypotenuse(3, 5) == 34
    assert calculate_hypotenuse(300, 5) == 90025
    with pytest.raises(ValueError, match="Parameter value cannot be negative"):
        calculate_hypotenuse(-5, -3)