class Numero():

    def __init__(self, numero):
        self.numero = numero

    def feliz(self):
        soma = self.soma_quadrados()
        if soma in range(10):
            return soma == 1
        return Numero(soma).feliz()

    def soma_quadrados(self):
        return sum([int(char)**2 for char in str(self.numero)])
#        soma = 0
#        for numero in str(self.numero):
#            soma += int(numero) ** 2
#        return soma
