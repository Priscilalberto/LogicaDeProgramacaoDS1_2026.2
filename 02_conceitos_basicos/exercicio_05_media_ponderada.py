"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:
nota_1 = float(input("digite a nota: "))
nota_2 = float(input("digite a nota: "))
nota_3 = float(input("digite a nota: "))
resultado = (nota_1*2)+(nota_2*3)+(nota_3*5)
final = (resultado/3)
print(f"a sua media é : {final:.2f}")