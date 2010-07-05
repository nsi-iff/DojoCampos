class WaterFlow:

    def __init__(self, litros_por_caixa, litros_por_segundo):
        self.litros_por_caixa = litros_por_caixa
        self.litros_por_segundo = litros_por_segundo

    def verificar_agua_no_tempo(self, tempo):
        self.litros_por_caixa[0] -= (self.litros_por_segundo*tempo)       
        self.litros_por_caixa[1] += (self.litros_por_segundo*tempo)
        if self.litros_por_caixa[0] < 0:
            self.litros_por_caixa[1] = self.litros_por_caixa[0] + self.litros_por_caixa[1]
            self.litros_por_caixa[0] = 0        
        return self.litros_por_caixa
