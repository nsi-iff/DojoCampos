from should_dsl import should, should_not
import unittest
import specloud

from vending_machine import VendingMachine

class TestVendingMachine(unittest.TestCase):
    def test_maquina_criada(self):
        maquina = VendingMachine()
        maquina.produtos.has_key('coca') |should| equal_to (True)
        maquina.produtos.has_key('fandangos') |should| equal_to (True)
        maquina.produtos.has_key('chetoos') |should_not| equal_to (True)

    def test_maquina_tem_produto(self):
        maquina = VendingMachine()
        maquina.tem_produto("chocolate") |should| equal_to (False)
        maquina.tem_produto("coca") |should| equal_to (True)
    def test_maquina_tem_chiclete(self):
        maquina = VendingMachine()
        maquina.tem_produto("chiclete") |should| equal_to (False)

    def test_compra_chocolate_com_50_cents(self):
        maquina = VendingMachine()
        maquina.comprar("chocolate", 0.50) |should| equal_to (False)

    def test_compra_coca_com_1_dolar(self):
        maquina = VendingMachine()
        maquina.comprar("coca", 1.0) |should| equal_to (True)

    def test_compra_coca_com_2_dolares(self):
        maquina = VendingMachine()
        maquina.comprar("coca",2.0) |should| equal_to(True)
        maquina.troco |should| equal_to (1)
