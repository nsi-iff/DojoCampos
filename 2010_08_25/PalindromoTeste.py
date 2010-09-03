import unittest
from palindromo import Palavra

class TestPalindromo(unittest.TestCase):

    def test_verdadeiro_quando_passar_haha(self):
        palavra = Palavra("haha")
        self.assertTrue(palavra.eh_palindromo())

    def test_falso_quando_passar_meu_ovo(self):
        palavra = Palavra("meu ovo")
        self.assertFalse(palavra.eh_palindromo())
    
    def test_verdadeiro_quando_passar_bombom(self):
        palavra = Palavra("bombom")
        self.assertTrue(palavra.eh_palindromo())

   

unittest.main()

