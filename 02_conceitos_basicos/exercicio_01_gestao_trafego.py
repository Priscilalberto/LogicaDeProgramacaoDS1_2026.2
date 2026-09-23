# """
# EXERCÍCIO 01: Gestão de Tráfego Casas Paulino
# Disciplina: Lógica de Programação com Python

# ENUNCIADO:
# A loja Casas Paulino está veiculando anúncios no Meta Ads em Tianguá.
# Escreva um programa que leia:
# 1. O valor total investido na campanha (em R$).
# 2. O número total de cliques obtidos.

# Calcule e mostre na tela o Custo Por Clique (CPC) médio da campanha formatado em reais.
# """

# TODO: Desenvolva o algoritmo abaixo:
valor_total = float(input("digite o valor total investido na campanha: "))
total__cliques = float(input("digite o numero total de cliques: "))
resposta = float(valor_total)/int(total__cliques)
print(f"{resposta:.2f} R$ por cliques")