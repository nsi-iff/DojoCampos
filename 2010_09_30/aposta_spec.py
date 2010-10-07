# coding: UTF-8

import unittest
from should_dsl import should
from aposta import Torneio


class TestTorneio(unittest.TestCase):

    def test_adicionar_times(self):
        carioca = Torneio()
        carioca.adicionar_time("Vasco")
        carioca.adicionar_time("Flamengo")
        carioca.lista_times |should| equal_to (['Vasco','Flamengo'])


    def test_definir_confronto(self):
        paulista = Torneio()
        paulista.adicionar_time("São Paulo")
        paulista.adicionar_time("Santos")
        paulista.confronto(["São Paulo", 3], ["Santos", 2])        
        paulista.total_pontos |should| equal_to ["São Paulo", 2]



