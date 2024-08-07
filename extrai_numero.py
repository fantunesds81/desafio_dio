import re


def extrai_numero (texto):
    padrao = r'\d+'
    return re.findall(padrao, texto)

frase = input('Digite a frase: ')
numeros = extrai_numero(frase)


for numero in numeros:
    print(numero)