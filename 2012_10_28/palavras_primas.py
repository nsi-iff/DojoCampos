def fatorPrimo(numero): 
    if numero in [0,1]:
        return False
    for x in range(2, (numero+2)/2):
        if numero % x == 0:
             return False
    return True
    
def palavra_prima(palavra):
  lista_letras= list  ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") 
  valor = 0
  for letra in palavra:
    if letra in (lista_letras):
      valor += lista_letras.index(letra) + 1
  return fatorPrimo(valor)

