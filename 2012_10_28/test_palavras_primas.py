import unittest
from should_dsl import should
from palavras_primas import palavra_prima

class TestPalavraPrima(unittest.TestCase):

  def test_de_nao_primo(self):
    palavra_prima('de') |should| equal_to(False)

  def test_casa_nao_primo(self):
    palavra_prima('casa') |should| equal_to(False)
    
  def test_c_nao_primo(self):
    palavra_prima('c') |should| equal_to(True)

  def test_guarda_chuva_e_primo(self):
    palavra_prima('guarda-chuva') |should| equal_to(True)
  def test_da_primo(self):
    palavra_prima('da') |should| equal_to (True)
