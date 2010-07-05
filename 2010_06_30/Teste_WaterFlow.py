import unittest
from WaterFlow import WaterFlow

class WaterFlowTestCase(unittest.TestCase):

    def test_litros_nas_caixas_no_tempo_0(self):
        fluxo = WaterFlow([10, 0], 1) #litros por caixa, litros por segundo no cano 
        self.assertEquals(fluxo.verificar_agua_no_tempo(0), [10, 0]) #tempo, quantidade de agua
    
    def test_litros_nas_caixas_no_tempo_2(self):
        fluxo = WaterFlow([10, 10], 5) #litros por caixa, litros por segundo no cano 
        self.assertEquals(fluxo.verificar_agua_no_tempo(3), [0, 20]) #tempo, quantidade de agua

    
    def test_litros_nas_caixas_no_tempo_1(self):
        fluxo = WaterFlow([10, 0], 1) #litros por caixa, litros por segundo no cano 
        self.assertEquals(fluxo.verificar_agua_no_tempo(1), [9, 1]) #tempo, quantidade de agua

    def test_litros_nas_caixas_no_tempo_6(self):
        fluxo = WaterFlow([10, 0], 3) #litros por caixa, litros por segundo no cano 
        self.assertEquals(fluxo.verificar_agua_no_tempo(6), [0, 10]) #tempo, quantidade de agua
    
if __name__ == "__main__":
    unittest.main()
