import pytest
import calculator


class TestCalculator:
    def test_add(self):
        assert calculator.add(1, 2) == 3
    def test_substract(self):
        assert calculator.subtract(1, 2) == -1
    def test_multiply(self):
        assert calculator.multiply(1, 2) == 2
    def test_divide(self):
        assert calculator.divide(1, 2) == 0.5
    def test_zeroDivision(self):
        with pytest.raises(ZeroDivisionError):
            calculator.divide(1, 0)