def jokenpo(jogada1, jogada2):
    jogadas = ("pedra","tesoura","papel")
    if jogada1 == jogada2:
        return "empate"
    elif jogada1 == jogadas[jogadas.index(jogada2) -1]:
        return jogada1
    else:
        return jogada2

#    if (jogada1 == 'papel' and jogada2 == 'pedra') or (jogada1 == 'pedra' and jogada2 == 'papel'):
#        return 'papel'
#    elif (jogada1 == 'papel' and jogada2 == 'tesoura') or (jogada1 == 'tesoura' and jogada2 == 'papel'):
#        return 'tesoura'
#    elif (jogada1 == 'pedra' and jogada2 == 'tesoura') or ():
#        return 'pedra'
#    elif jogada1 == 'tesoura' and jogada2 == 'pedra':
#        return 'pedra'

