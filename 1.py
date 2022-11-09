class No:

    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None

class Lista:
    
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho


    def inserir_dado(self, valor):
        no = No(valor)
        if self.inicio:
            pointer = self.inicio
            while (pointer.next):
                pointer = pointer.next

            pointer.next = No(valor)
        else:
            no = No(valor)
        self.tamanho += 1

lista = Lista()
lista.inserir_dado(7)
lista.tamanho()
lista.inserir_dado(5)