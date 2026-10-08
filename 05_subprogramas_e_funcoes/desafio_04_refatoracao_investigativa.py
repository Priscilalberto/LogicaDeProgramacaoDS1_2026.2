"""
DESAFIO 04: REFATORAÇÃO INVESTIGATIVA
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
O código monolítico repete cálculos de desconto e impostos várias vezes.

SUA MISSÃO:
1. Crie uma função calcular_preco_final(preco_base, taxa_desc, taxa_imp) com return.
2. Crie um procedimento exibir_relatorio_item(numero_item, preco_final) com print.
3. Teste suas funções refatoradas.
"""

# TODO: Desenvolva as funções modulares abaixo:
def calcular_preco_final(preco_base, taxa_desc, taxa_imp):
    desconto = preco_base * taxa_desc
    preco_com_desconto = preco_base - desconto
    imposto = preco_com_desconto * taxa_imp
    return preco_com_desconto + imposto


def exibir_relatorio_item(numero_item, preco_final):
    print("Item", numero_item, "- Preço final: R$", preco_final)


# Teste
preco = calcular_preco_final(100, 0.10, 0.05)
exibir_relatorio_item(1, preco)