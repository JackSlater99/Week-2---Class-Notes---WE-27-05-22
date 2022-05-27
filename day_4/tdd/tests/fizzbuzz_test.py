import unittest
from src.fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_3_returns_fizz(self):
        self.assertEqual("Fizz", fizzbuzz(3))

    def test_6_returns_fizz(self):
        self.assertEqual("Fizz", fizzbuzz(6))
    
    def test_5_returns_buzz(self):
        self.assertEqual("Buzz", fizzbuzz(5))

    def test_10_returns_buzz(self):
        self.assertEqual("Buzz", fizzbuzz(10))

    def test_30_returns_fizzbuzz(self):
        self.assertEqual("FizzBuzz", fizzbuzz(30))

    def test_150_returns_fizzbuzz(self):
        self.assertEqual("FizzBuzz", fizzbuzz(150))

    def test_returns_1_as_string(self):
        self.assertEqual("1", fizzbuzz(1))

    def test_returns_2_as_a_string(self):
        self.assertEqual("2", fizzbuzz(2))