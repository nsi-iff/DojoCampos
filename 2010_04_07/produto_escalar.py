class ListasComTamanhosDiferentes(Exception):
    pass

def multiplica_vetores(vetor1, vetor2):
    if len(vetor1)!=len(vetor2):
        raise ListasComTamanhosDiferentes('Vetores de tamanhos diferentes!')

    resultado = 0
    for i in range(len(vetor1)):
        resultado += vetor1[i] * vetor2[i]
    return resultado

