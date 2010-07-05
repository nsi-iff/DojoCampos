#coding:utf-8

class RomanRoullete(object):
    

    def __init__(self, pessoas, execucao):
        self.lista_de_pessoas = []
        for it in range(pessoas):
            self.lista_de_pessoas.append(1)
        self.pessoas = pessoas
        self.matar = execucao
        self.passos_faltantes = execucao

    def executar_pessoas(self):
        if sum(self.lista_de_pessoas)==1:
            return self.lista_de_pessoas.index(1)
        else:
            for x in range(len(self.lista_de_pessoas)):
                while self.lista_de_pessoas.index(1, self.lista_de_pessoas[x]) and self.passos_faltantes<>1:
                    self.passos_faltantes-=1
                while self.lista_de_pessoas.index(1, self.lista_de_pessoas[x])==1 and self.passos_faltantes==1:
                    self.lista_de_pessoas[x]=0
                    self.passos_faltantes = self.matar
            self.executar_pessoas()
