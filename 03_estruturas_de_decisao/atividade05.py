# TODO: Implemente o menu utilizando match-case ou elif
opcao = int(input("Digite a opção desejada (1, 2 ou 3): "))

# Desenvolva a estrutura de seleção aqui

match opcao :
    case 1:
        print("Você escolheu a opção 1.")
    case 2:
        print("Você escolheu a opção 2.")
    case 3:
        print("Você escolheu a opção 3.")
    case _:
        print("Opção inválida.")