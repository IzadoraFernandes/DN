class No:
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = None

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)


class Pilha:
    def __init__(self):
        self.cabeca = None


    def __repr__(self):
        return  str(self.topo) 

    def inserir(self, novo_dado):  
      novo_nodo = No(novo_dado)
      novo_nodo.anterior = self.topo
      self.topo = novo_nodo


pilha = Pilha()
print("Pilha vazia: ", pilha)


for i in range(5):
  number = input("\nDigite um número: ")
  pilha.inserir(number)
  print(pilha)  
