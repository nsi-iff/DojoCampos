class Banheiro:

  def __init__(self, vagas):
    self.list = [False]*vagas

  def distribuicao(self, homens):
    if homens >= 1:
      self.list[-1] = 0
    if homens >= 2:
      self.list[0] = 1
    if homens >= 3:
      self.list[2] = 2  
    return self.list
