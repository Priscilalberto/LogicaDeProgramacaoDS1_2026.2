# TODO: Defina a função calcular_media e teste-a abaixo
from unittest import result


def calcular_media(nota1, nota2, nota3):
    # Escreva o corpo da função
    media = (nota1 + nota2 + nota3) /3
    return media

# Teste com notas de exemplo
resultado = calcular_media(8, 7, 9)
print("Média:",resultado)