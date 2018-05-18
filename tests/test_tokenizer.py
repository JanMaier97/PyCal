import pytest

from pycal.tokenize import tokenize


def test_simple_addition():
    assert tokenize("10 + 5") == [10, "+", 5]


def test_simple_subtraction():
    assert tokenize("10 - 5") == [10, "-", 5]


def test_simple_multiplication():
    assert tokenize("10 * 5") == [10, "*", 5]


def test_simple_division():
    assert tokenize("10 / 5") == [10, "/", 5]


def test_simple_modulo():
    assert tokenize("10 % 5") == [10, "%", 5]


def test_simple_exponent():
    assert tokenize("10 ** 5") == [10, "**", 5]


def test_simple_function():
    assert tokenize("sin(23)") == ["sin", "(", 23, ")"]


def test_complex_expression():
    expression = "10 * (20 + 100) / sin(x + 8 ** 2)"
    assert tokenize(expression) == [10, '*', '(', 20, '+', 100, ')', '/',
                                    'sin', '(', 'x', '+', 8, '**', 2, ')']
