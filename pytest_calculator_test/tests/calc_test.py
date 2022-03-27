import pytest
from app.calculator import Calculator

class TestCalculator:
    def setup(self):
        self.calculator = Calculator

# позитивный тест умножения
    def test_multiply_calculate_correctly(self):
        assert self.calculator.multiply(self, 2, 2) == 4

# позитивный тест деления
    def test_division_calculate_correctly(self):
        assert self.calculator.division(self, 6, 2) == 3

# позитивный тест вычитания
    def test_subtraction_calculate_correctly(self):
        assert self.calculator.subtraction(self, 8, 4) == 4

# позитивный тест сложения
    def test_adding_calculate_correctly(self):
        assert self.calculator.adding(self, 5, 5) == 10

# позитивный тест вычисление корня
    def test_square_root_calculate_correctly(self):
        assert self.calculator.square_root(self, 25) == 5
