
def fatorPrimo(numero): 
    if numero in [0,1]:
        return False
    for x in range(2, (numero+2)/2):
        if numero % x == 0:
             return False
    return True
#fatorPrimo = lambda n: not(n in [0,1]) and all(n%x!=0 for x in range(2, (n+2)/2))
