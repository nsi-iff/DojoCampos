import unittest 
from should_dsl import should
from jokenpo import jokenpo

class TestJokenpo(unittest.TestCase):

    def test_papel_versus_pedra(self):
        jokenpo('papel','pedra') |should| equal_to('papel')

    def test_papel_versus_tesoura(self):
        jokenpo('papel', 'tesoura') |should| equal_to('tesoura')
    
    def test_pedra_versus_tesoura(self):
        jokenpo('pedra', 'tesoura') |should| equal_to ('pedra')
        
    def test_pedra_versus_papel(self):
        jokenpo('pedra', 'papel') |should| equal_to ('papel')
    def test_tesoura_versus_papel(self):
        jokenpo('tesoura', 'papel') |should| equal_to ('tesoura')
    def test_tesoura_versus_pedra(self):
        jokenpo('tesoura','pedra') |should| equal_to('pedra') 
