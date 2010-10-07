jogadas = [("pedra", "tesoura"), ("papel", "pedra"), ("tesoura", "papel")]
def jogo(mao1,mao2):
    if mao1 == mao2:
        return "empate"
    for i0, i1 in jogadas:
        if (i0 == mao1 and i1 == mao2) or \
           (i0 == mao2 and i1 == mao1):
            return i0
