# Random number

import random

valor_aleatorio = random.randint(1, 10)
# tentativas = 0
valor = 0


def recebendo_numero(valor):
    numero = int(input("Digite um numero de 1 a 10, você tem apenas 4 tentativas: "))
    if numero <= 10:
        if numero > valor_aleatorio:
            print("O numero escolhido é maior que o valor gerado")
            # tentativas = int(tentativas) + 1
            return False
        elif numero < valor_aleatorio:
            print("o o numero escolhido é menor que o valor gerado")
            # tentativas = tentativas + 1
            return False
        elif numero == valor_aleatorio:
            return True
            print(" O numero escolhido é igual ao valor gerado")



    else:
        print("Coloque um numero entre 1 e 10")


# if tentativas == 4:
# print("\nAcabou as tentativas")

acertou = bool(recebendo_numero(valor))
while (acertou == False):
    recebendo_numero(valor)
    print(bool(acertou))

print(valor)
