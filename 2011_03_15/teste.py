import unittest
from should_dsl import *
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_quando_entrar_com_1_retornar_1(self):
        fizzbuzz(1) |should| equal_to(1)

    def test_quando_entrar_com_3_retornar_fizz(self):
        fizzbuzz(3) |should| equal_to("fizz")

    def test_quando_entrar_com_6_retornar_fizz(self):
        fizzbuzz(6) |should| equal_to("fizz")

    def test_quando_entrar_com_5_retornar_buzz(self):
        fizzbuzz(5) |should| equal_to("buzz")

    def test_quando_entrar_com_10_retornar_buzz(self):
        fizzbuzz(10) |should| equal_to("buzz")

    def test_quando_entrar_com_15_retornar_fizzbuzz(self):
        fizzbuzz(15) |should| equal_to("fizzbuzz")

if __name__ == "__main__":
    unittest.main()
