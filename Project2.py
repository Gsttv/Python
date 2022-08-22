# Random number

import random
numero = int(input("Digite um numero de 1 a 10"))
valor_aleatorio = random.randint(1,10)

if numero>=1 and numero<=10:
    if numero>valor_aleatorio:
        print("O numero escolhido é maior que o valor gerado")
        print(valor_aleatorio)
    elif numero<valor_aleatorio:
        print("o o numero escolhido é menor que o valor gerado")
        print(valor_aleatorio)
    elif numero == valor_aleatorio:
        print(" O numero escolhido é igual ao valor gerado")

else:
    print("O numedo escolhido deve estar entre 1 e 10 ")
