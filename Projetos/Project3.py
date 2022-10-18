# Speed Meter

valor_veloc = int(input("Digite o valor da velocidade:  "))
veloc_max = 80

if valor_veloc <= veloc_max:
    print("Você não levou multa")
elif valor_veloc > veloc_max and valor_veloc <= veloc_max + 10:
    print("Você levou uma multa leve")
elif valor_veloc > veloc_max + 10 and valor_veloc <= veloc_max + 20:
    print("Você levou uma multa grave")
elif valor_veloc > veloc_max + 20:
    print("Você levou uma multa gravissima")

