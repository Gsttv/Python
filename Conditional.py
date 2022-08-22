#Conditional
primeiro_valor = input('Digite o Primeiro valor')
segundo_valor = input('Digite o Segundo valor')
if int(primeiro_valor) > int(segundo_valor):
  print("O primeiro valor é maior q o segundo")
elif int(segundo_valor) > int(primeiro_valor):
  print("O segundo valor é maior q o  primeiro")
elif int(primeiro_valor) == int(segundo_valor):
  print("Os valores são iguais")