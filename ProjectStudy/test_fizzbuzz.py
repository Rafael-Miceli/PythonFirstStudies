import unittest
from FizzBuzz import FizzBuzzStudy

__author__ = 'rafael.miceli'


class TestFizzBuzz(unittest.TestCase):

    def test_should_return_fizz_when_multiple_of_3(self):

        num = 9
        fizz_buzz_study = FizzBuzzStudy()

        result = fizz_buzz_study.is_fizz_or_buzz(num)

        self.assertEqual("fizz", result)

    def test_should_return_buzz_when_multiple_of_5(self):
        num = 10
        fizz_buzz_study = FizzBuzzStudy()

        result = fizz_buzz_study.is_fizz_or_buzz(num)

        self.assertEqual("buzz", result)

    def test_should_return_number_when_not_multiple_of_5_or_3(self):
        num = 7
        fizz_buzz_study = FizzBuzzStudy()

        result = fizz_buzz_study.is_fizz_or_buzz(num)

        self.assertEqual(num, result)

    def test_should_return_fizzbuzz_when_multiple_of_5_and_3(self):
        num = 30
        fizz_buzz_study = FizzBuzzStudy()

        result = fizz_buzz_study.is_fizz_or_buzz(num)

        self.assertEqual("fizzbuzz", result)

    def test_100_fizzbuzz_call(self):
        fizz_buzz_study = FizzBuzzStudy()
        fizz_buzz_study._100_fizz_buzz_calls()



if __name__ == "__main__":
    unittest.main()
