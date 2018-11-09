from example1_pytest_intro import app
import pytest
import sys


# @pytest.mark.skipif(sys.version_info > (3, 6), reason="I don't want to run this test at the moment")
@pytest.mark.windows
def test_calc_total():
    total = app.calc_total(4, 5)
    assert total == 9


@pytest.mark.windows
def test_calc_multiply():
    assert app.calc_multiply(2, 3) == 6


@pytest.mark.mac
def test_dummy():
    assert True
