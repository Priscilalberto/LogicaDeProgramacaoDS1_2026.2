"""
EXERCÍCIO 02: Consumo da Kawasaki Versys 300
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Para planejar uma viagem técnica de Tianguá até o Beach Park (Aquiraz),
solicite:
1. A distância total percorrida (em Km).
2. O total de combustível gasto (em Litros).

Calcule e imprima o consumo médio da motocicleta (Km/L) formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
distancia_total = float(input("qual a distância total percorrido na viagem?"))
total_de_combustivel = float(input("total de combustivel gasto?"))
resposta = distancia_total/total_de_combustivel
print(f"total de consumo medio{resposta:.2} km/L")