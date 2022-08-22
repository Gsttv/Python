# Random number

import random
valor_aleatorio = random.randint(1,10)

acertou = False


while acertou == False:
        numero = int(input("Digite um numero de 1 a 10"))

        if numero > valor_aleatorio:
           print("O numero escolhido é maior que o valor gerado")


        elif numero<valor_aleatorio:
            print("o o numero escolhido é menor que o valor gerado")


        elif numero == valor_aleatorio:
            acertou = True
            print(" O numero escolhido é igual ao valor gerado")


