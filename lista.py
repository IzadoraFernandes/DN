class NodoLista:
    """Esta classe representa um nodo de uma lista encadeada."""
    def __init__(self, dado=0, proximo_no=None):
        self.dado = dado
        self.proximo = proximo_no

    def __repr__(self):
        
        return (f"  {self.dado} -> {self.proximo}")
        
class ListaEncadeada:

    def __init__(self):
        self.cabeca = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"
        
    def insere_no_inicio(lista, novo_dado):
        # 1) Cria um novo no com o dado a ser armazenado.
        novo_no = NodoLista(novo_dado)
    
        # 2) Faz com que o novo no seja a cabeça da lista.
        novo_no.proximo = lista.cabeca
    
        # 3) Faz com que a cabeça da lista referencie o novo no.
        lista.cabeca = novo_no

    def remove(self, valor):
        assert self.cabeca, "Impossível remover valor de lista vazia."

        # Nodo a ser removido é a cabeça da lista.
        if self.cabeca.dado == valor:
            self.cabeca = self.cabeca.proximo
        else:
            # Encontra a posição do elemento a ser removido.
            anterior = None
            corrente = self.cabeca
            while corrente and corrente.dado != valor:
                anterior = corrente
                corrente = corrente.proximo
            # O nodo corrente é o nodo a ser removido.
            if corrente:
                anterior.proximo = corrente.proximo
            else:
                # O nodo corrente é a cauda da lista.
                anterior.proximo = None

    def insere_depois(lista, nodo_anterior, novo_dado):
        assert nodo_anterior, "Nodo anterior precisa existir na lista."

        # Cria um novo nodo com o dado desejado.
        novo_nodo = NodoLista(novo_dado)

        # Faz o próximo do novo nodo ser o próximo do nodo anterior.
        novo_nodo.proximo = nodo_anterior.proximo

        # Faz com que o novo nodo seja o próximo do nodo anterior.
        nodo_anterior.proximo = novo_nodo

    def busca(lista, valor):
        corrente = lista.cabeca
        while corrente and corrente.dado != valor:
            corrente = corrente.proximo
        return corrente
        
lista = ListaEncadeada()
print("Lista vazia:", lista)

lista.insere_no_inicio( 5)
print("Lista contém um único elemento:", lista)

lista.insere_no_inicio( 10)
print("Inserindo um novo elemento:", lista)

lista.insere_no_inicio( 7)
print("Inserindo um novo elemento:", lista)