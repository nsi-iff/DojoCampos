class VendingMachine():
    def __init__(self):
        self.produtos = {'coca':1.0,
                         'fandangos':0.25}

    def empty(self):
        if self.produtos:
            return True

    def tem_produto(self, produto):        
        return self.produtos.has_key(produto)       
           
    def comprar(self, produto, dinheiro):
        if self.produtos[produto] == dinheiro:
            return True
        else:
            produto = self.produtos[produto]
            self.troco = dinheiro-produto
            return True
            
