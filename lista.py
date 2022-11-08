class NodoLista:
    """Esta classe representa um nodo de uma lista encadeada."""
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)
        
class ListaEncadeada:
    """Esta classe representa uma lista encadeada."""
    def __init__(self):
        self.cabeca = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"
        
    def insere_no_inicio(lista, novo_dado):
        # 1) Cria um novo no com o dado a ser armazenado.
        novo_nodo = NodoLista(novo_dado)
    
        # 2) Faz com que o novo no seja a cabeça da lista.
        novo_nodo.proximo = lista.cabeca
    
        # 3) Faz com que a cabeça da lista referencie o novo no.
        lista.cabeca = novo_nodo

    def apagar(lista, dado):
        pass
        
lista = ListaEncadeada()
print("Lista vazia:", lista)

lista.insere_no_inicio( 5)
print("Lista contém um único elemento:", lista)

lista.insere_no_inicio( 10)
print("Inserindo um novo elemento:", lista)

lista.insere_no_inicio( 7)
print("Inserindo um novo elemento:", lista)