import random

def menu():
    print('''    ###################
    #                #
    #                #
    #              ######
    #                
    #                
    #               
    #                
    #                
    #                
    ''',end="")
    for item in tracos:
        print("  ", item, end=" ")

fruta = ["5banana", "maça", "pera", "uva", "abacaxi", "abacate", "amora", "ameixa", "acerola", "carambola"]
animais = ["cachorro", "gato", "coruja", "leão", "tigre", "capivara", "peixe", "gavião", "leopardo"]
objeto = ["estojo", "caneta", "lapis", "mouse", "grampeador"]
letra_digitada = []
opcoes = [fruta, animais, objeto]
n = input('''           -------------------------------
                    JOGO DA FORCA          
           -------------------------------
    Digite o numero da opção do tema que deseja jogar: 
                    0 - Fruta
                    1 - Animal
                    2 - Objeto

obs: Coloque a acentuação correta
''')
n = int(n)
escolha = opcoes[n]

elemento = random.choice(escolha)
elemento2 = list(elemento)

tracos = list("-" * len(elemento2))
menu()

while True:
    letra = input("\ndigite a letra: ")
    if letra in letra_digitada:
        print('você já escolheu essa letra')
        continue
    else:
        letra_digitada.append(letra)
        for idx, item in enumerate(elemento):
            if letra == item:
                # q = elemento.index(letra)
                tracos.__delitem__(idx)
                tracos.insert(idx, letra)
    menu()
    if tracos == list(elemento):
        break



