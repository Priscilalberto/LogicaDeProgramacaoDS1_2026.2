# TODO: Desenvolva o acumulador com parada no 0
soma = 0

# Escreva a estrutura de repetição while
numero = int(input("Digite um número (0 para parar): "))

while numero != 0:
    soma += numero
    numero = int(input("Digite um número (0 para parar): "))

print("Soma:", soma)