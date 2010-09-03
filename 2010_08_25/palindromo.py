class Palavra:
    def __init__(self, palavra_externa):
        self.palavra = palavra_externa

    def eh_palindromo(self):
        silaba1 = self.palavra[0:(len(self.palavra)/2)-1]
        silaba2 = self.palavra[len(self.palavra)/2:]

        if silaba1 == silaba2:
            return True
        else:
            return False
