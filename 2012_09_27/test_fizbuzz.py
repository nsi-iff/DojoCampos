import unittest
from should_dsl import should
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

  def test_tres_retorna_fizz(self):
    fizzbuzz(3) |should| equal_to("Fizz")
  
  def test_cinco_retorna_buzz(self):
    fizzbuzz(5) |should| equal_to('Buzz')

  def test_quinze_retorna_fizzbuzz(self):
    fizzbuzz(15) |should| equal_to ('FizzBuzz')
     
  def teste_seis_retorna_fizz(self):
    fizzbuzz(6) |should| equal_to('Fizz')
    
  def teste_dez_retorna_buzz(self):
    fizzbuzz(10) |should| equal_to ('Buzz')
  
  def teste_sete_retorna_nada(self):
    fizzbuzz(7) |should| equal_to("")
  
  
if __name__ == '__main__':
  unittest.main()
