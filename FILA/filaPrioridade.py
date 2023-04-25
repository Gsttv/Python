import numpy as np

class FilaPrioridade:
    def __init__(self,capacidade):
        self.capacidade = capacidade
        self.numeroElementos = 0
        self.valores = np.empty(self.capacidade,dtype=int)

    def __filaVazia(self):
        return self.numeroElementos == 0
    def __filaCheia(self):
        return self.numeroElementos == self.capacidade-1
