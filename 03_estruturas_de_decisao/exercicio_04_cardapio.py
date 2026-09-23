"""
EXERCÍCIO 04: Cardápio da Lanchonete
Disciplina: Lógica de Programação com Python

TABELA:
1 - Cachorro Quente: R$ 4.00
2 - X-Salada: R$ 4.50
3 - X-Bacon: R$ 5.00
4 - Torrada Simples: R$ 2.00
5 - Refrigerante: R$ 1.50

ENUNCIADO:
Leia o código do item e a quantidade consumida.
Calcule e mostre o total a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
codigo = int(input("Digite o código do item: "))
quantidade = int(input("Digite a quantidade: "))
if codigo == 1:
    preco = 4.00
elif codigo == 2:
    preco = 4.50
elif codigo == 3:
    preco = 5.00
elif codigo == 4:
    preco = 2.00
elif codigo == 5:
    preco = 1.50
else:
    preco = 0
total = preco * quantidade
print(f"Total: R$ {total:.2f}")