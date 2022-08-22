# Factorial of a Number

numero = int(input("Digite o numero"))
if numero > 0:
    fatorial = 1
    for item in range(1,numero+1):
        fatorial = fatorial*item

    print(fatorial)
else:
    print(" O numero deve ser positivo")
