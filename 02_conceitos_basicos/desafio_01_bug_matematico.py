"""

DESAFIO 01: O BUG MATEMÁTICO DA MÉDIA ESCOLAR
Disciplina: Lógica de Programação com Python
EEEP Professor Sebastião Vasconcelos Sobrinho

RELATÓRIO DA INVESTIGAÇÃO:
Um estágiário do sistema acadêmico tentou implementar o cálculo da média semestral de um aluno, mas o sistema apresentou resultados bizarros devido a erros de tipagem e precedência de operadores.

SUA MISSÃO:
1. Indentifique e corrija os erros de tipagem (casting) e precedência.
2. Faça o programa calculanr e exibir a média correta formatada com 1 casa decimal.
"""

# CÓDIGO ORIGINAL COM BUG (Analilise e corrija):
# nota1 = input("Digite a primeira nota: ")
# nota2 = input("Digite a segunda nota: ")
# media = nota1 + nota2 / 2
# print("A média do aluno é:", media")

#TODO: escreva aqui o código corrigido:
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
media = (nota1+nota2)/2
print(f"A média do aluno é:{media:.1f}")