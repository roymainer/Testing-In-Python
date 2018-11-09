from example3_pytest_parameters import mathlib
import pytest


# instead of copying a lot of code
# def test_calc_square_1():
#     assert mathlib.calc_square(5) == 25
#
#
# def test_calc_square_2():
#     assert mathlib.calc_square(6) == 36
#
#
# def test_calc_square_3():
#     assert mathlib.calc_square(10) == 100


@pytest.mark.parametrize("test_input, expected_output",
                          [(5, 25), (6, 36), (10, 100)])  # a list of tuples, containing inputs and expected outputs
def test_calc_square(test_input, expected_output):
    assert mathlib.calc_square(test_input) == expected_output
