lista = [("tesoura","papel"),("papel","pedra"),("pedra","tesoura")]

def jokenpo(mao_um, mao_dois):
    for i in lista:
        if (mao_um, mao_dois) == i or (mao_dois, mao_um) == i:
            return i[0]
    return "empate"
