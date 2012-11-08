import unittest
from should_dsl import should
from mictorio import Banheiro


class TestMictorio(unittest.TestCase):


  def test_1_homem_para_5_vagas(self):
    banheiro = Banheiro(5)
    resultado = banheiro.distribuicao(1)
    resultado |should| equal_to([False, False, False, False, 0])
    
  def test_2_homens_para_5_vagas(self):
    banheiro = Banheiro(5)
    resultado = banheiro.distribuicao(2)
    resultado |should| equal_to([1, False, False, False, 0])

  def test_3_homens_para_5_vagas(self):
    banheiro = Banheiro(5)
    resultado = banheiro.distribuicao(3)
    resultado |should| equal_to([1, False, 2, False, 0])
