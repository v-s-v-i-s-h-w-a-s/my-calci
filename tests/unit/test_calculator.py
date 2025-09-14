"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import pytest
from src.calculator import add, subtract

class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25

    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        assert add(-1, -1) == -2
        assert add(-5, 3) == -2
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6
    
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers"""
        assert subtract(-1, -1) == 0
        assert subtract(-5, -3) == -2

# TODO: Students will add TestMultiplyDivide class