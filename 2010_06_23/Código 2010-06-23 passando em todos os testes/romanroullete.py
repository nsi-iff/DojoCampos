#coding:utf-8

class RomanRoullete(object):

    def __init__(self, pessoas, intervalo_para_matar):
        self.lista_de_pessoas = []
        for pessoa in range(pessoas):
            self.lista_de_pessoas.append(1)
        self.intervalo_para_matar = intervalo_para_matar
        self.passos_faltantes = intervalo_para_matar

    def executar_pessoas(self):
          for x in range(len(self.lista_de_pessoas)):
            if self.lista_de_pessoas.index(1, self.lista_de_pessoas[x]) and self.passos_faltantes > 1:
                self.passos_faltantes -= 1            
                
            elif self.lista_de_pessoas.index(1, self.lista_de_pessoas[x]) and self.passos_faltantes == 1:
                self.lista_de_pessoas[x] = 0          
                self.passos_faltantes = self.intervalo_para_matar

            if (x == len(self.lista_de_pessoas) - 1 and sum(self.lista_de_pessoas) > 1):
                self.executar_pessoas()  
            
            if sum(self.lista_de_pessoas) == 1:                       
                return self.lista_de_pessoas.index(1)

