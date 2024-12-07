import pytest

from main.ini_4 import sum_all_odd_in_between

def test_sum_all_odd_in_between():
    assert sum_all_odd_in_between(100, 200) == 7500
