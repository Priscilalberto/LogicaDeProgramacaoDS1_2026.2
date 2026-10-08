"""
EXERCÍCIO 01: Pontuação OBI (Astro Lume Devs)
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma função nomeada `calcular_pontuacao_total(fase1, fase2, fase3)` com a diretiva `def`
que receba as 3 notas como parâmetros e retorne a pontuação total da equipe.
"""

# TODO: Desenvolva a função e os testes abaixo:
def calcular_pontuacao_total(fase1, fase2, fase3):
    return fase1 + fase2 + fase3


# Testes
pontuacao = calcular_pontuacao_total(10, 20, 30)
print("Pontuação total:", pontuacao)