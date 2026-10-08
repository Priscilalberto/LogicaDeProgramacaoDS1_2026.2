"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:
def calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel):
    litros = distancia_km / consumo_kml
    return litros * preco_combustivel


def calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao):
    return qtd_pessoas * dias * diaria_alimentacao


# Programa principal
distancia = float(input("Digite a distância da viagem (km): "))
consumo = float(input("Digite o consumo do veículo (km/l): "))
preco = float(input("Digite o preço do combustível: "))

pessoas = int(input("Digite a quantidade de pessoas: "))
dias = int(input("Digite a quantidade de dias: "))
diaria = float(input("Digite a diária de alimentação por pessoa: "))

custo_transporte = calcular_custo_transporte(distancia, consumo, preco)
custo_alimentacao = calcular_custo_alimentacao(pessoas, dias, diaria)

custo_total = custo_transporte + custo_alimentacao

print("Custo total da viagem: R$", custo_total)