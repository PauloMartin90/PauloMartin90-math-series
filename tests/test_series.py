
import pytest
from math_series.series import fibonacci, lucas, sum_series

def test_fib_1():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_fib_2():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected

def test_lucas_1():
    actual = lucas(5)
    expected = 11
    assert actual == expected
    
def test_sum_series_1():
    actual = sum_series(5)
    expected = 5
    assert actual == expected

def test_sum_series_2():
    actual = sum_series(5, 2, 1)
    expected = 11
    assert actual == expected