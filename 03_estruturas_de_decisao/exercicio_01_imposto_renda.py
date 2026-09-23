"""
EXERCÍCIO 01: Imposto de Renda de Lisarb
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de uma pessoa em Rombus (R$).
- Até R$ 2000.00: Isento
- De R$ 2000.01 até R$ 3000.00: 8% sobre o excedente de R$ 2000.00
- De R$ 3000.01 até R$ 4500.00: 18% sobre o excedente de R$ 3000.00 + 8% da faixa anterior
- Acima de R$ 4500.00: 28% sobre o que ultrapassar R$ 4500.00 + impostos anteriores

Imprima "Isento" ou o valor total do imposto formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
salario = float(input("Informe o salário:R$ "))
if salario <= 2000:
    print("Isento")
elif salario <= 3000:
    imposto = (salario - 2000) * 0.08
    print(f"{imposto:.2f}")
elif salario <= 4500:
    imposto = 1000 * 0.08 + (salario - 3000) * 0.18
    print(f"{imposto:.2f}")
else:
    imposto = 1000 * 0.08 + 1500 * 0.18 + (salario - 4500) * 0.28
    print(f"{imposto:.2f}")