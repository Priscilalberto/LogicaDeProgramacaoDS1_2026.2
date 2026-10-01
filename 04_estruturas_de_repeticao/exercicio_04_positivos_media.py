"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
quantidade = 0
soma = 0

for i in range(6):
    numero = float(input("Digite um valor: "))

    if numero > 0:
        quantidade += 1
        soma += numero

if quantidade > 0:
    media = soma / quantidade
else:
    media = 0

print(quantidade, "valores positivos")
print(f"{media:.1f}")
