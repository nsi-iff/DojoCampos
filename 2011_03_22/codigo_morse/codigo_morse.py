dicionario = {'a': '._', 'b': '_...', 'c': '_._.', 'w': '.__', 'e': '.', 
'l': '._..', 'm': '__', 'r':'._.', 'y': '_.__', 'g':'__.', 's': '...'}

def codigo_morse(palavra):
    palavra_morse = ''
    for letra in palavra:
        palavra_morse += dicionario[letra]
    return palavra_morse


