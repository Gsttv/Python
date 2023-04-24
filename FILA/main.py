import numpy as np


class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = 0
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __filaVazia(self):
        return self.numero_elementos == 0

    def __filaCheia(self):
        return self.numero_elementos == self.capacidade

    def enfilerar(self, valor):
        if self.__filaCheia():
            print("A fila esta cheia")
            return
        if self.final == self.capacidade - 1:
            self.final = -1
        self.final += 1
        self.valores[self.final] = valor
        self.numero_elementos += 1
    def desenfilerar(self):
        if self.__filaVazia():
            print("Fila esta vazia")
            return
        temp = self.valores[self.inicio]
        self.inicio+=1
        if self.inicio == self.capacidade -1:
            self.inicio = 0
        else:
            self.numero_elementos -=1
            return temp
    def primerio(self):
        if self.__filaVazia():
            print("A fila esta vazia")
        else:
            return self.valores[self.inicio]

