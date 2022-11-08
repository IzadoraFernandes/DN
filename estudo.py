
#   Lista - Lista encadeada

#Na classe trabalha-se com índice, ou seja, de 0 a tamanho - 1
#Ao chamar as funções trabalha-se com posições, ou seja, de 1 a tamanho

class NODO:
    def __init__(self, elemento, proximo):
        self.elemento = elemento
        self.proximo = proximo

class LISTA:
    def __init__(self):
        NODO.__init__(self, elemento = None, proximo = None)
        self.inicio = None
        self.tamanho = 0
    
    def __len__(self):
        return self.tamanho

    def MOSTRAR(self):
        listaAux = []
        add = None
        aux = self.inicio
        if(aux == None):
            return False
        else:
            while (aux != None):
                add = aux.elemento
                listaAux.append(add)
                aux = aux.proximo
            return listaAux
    
    def BUSCAR_POS(self, valor):
        aux = self.inicio
        posicao = 0
        contador = 0
        for i in range (self.tamanho):
            if (aux.elemento == valor):
                contador = 0
                return posicao + 1
            else:
                contador = contador + 1
            posicao = posicao + 1
            aux = aux.proximo
        if (contador == 0):
            return posicao + 1
        else:
            print ("Valor não presente!")
            return None
    
    def BUSCAR_VAL(self, posicao):
        aux = self.inicio
        contador = 0
        valor = 0
        if((posicao <= 0) or (posicao > self.tamanho)):
            print("Posição inválida.")
            return False
        else:
            posicao = posicao - 1
            for i in range(posicao + 1):
                if(contador == posicao):
                    valor = aux.elemento
                    break
                else:
                    aux = aux.proximo
                    contador = contador + 1
            return valor

    def INSERIR(self, valor, posicao):
        posicao = posicao - 1
        if ((posicao < 0) or (posicao > self.tamanho)):
            print ("Posição inválida!")
            return False
        elif (posicao == 0):
            self.inicio = NODO (valor, None)
        else:
            aux = self.inicio
            for i in range (1, posicao):
                aux = aux.proximo
            aux.proximo = NODO (valor, aux.proximo)
        self.tamanho = self.tamanho + 1
        return True

    def REMOVER(self, posicao):
        posicao = posicao - 1
        aux = 0
        remover = 0
        if((posicao < 0) or (posicao >self.tamanho)):
            print("Posição inválida!")
            return False
        elif(posicao == 0):
            
            remover = self.inicio
            self.inicio = self.inicio.proximo
            self.tamanho = self.tamanho - 1
            return remover
        else:
            aux = self.inicio
            for i in range(1, posicao):
                aux = aux.proximo
            remover = aux.proximo.elemento
            aux.proximo = aux.proximo.proximo
            self.tamanho = self.tamanho - 1
            return remover
    
    def DESTRUIR(self):
        self.elemento = None
        self.inicio = None
        self.proximo = None
        self.tamanho = 0
        
        
#FUNÇÕES EXTRAS


def Comparar(lista1, lista2):
    tamanho1 = lista1.TAMANHO()
    tamanho2 = lista2.TAMANHO()
    if(tamanho1 != tamanho2):
        print("As listas não são iguais.")
        return False
    else:
        aux1 = lista1.inicio
        aux2 = lista2.inicio
        contador = 0
        for i in range(tamanho1):
            if(aux1.elemento != aux2.elemento):
                contador = contador + 1
            aux1 = aux1.proximo
            aux2 = aux2.proximo
        if(contador > 0):
            print("As listas não são iguais.")
            return False
        else:
            print("Listas iguais")
            return True

def Inverso(lista1):
    tamanho = lista1.TAMANHO()
    aux = lista1.inicio
    l1 = []
    get = 0
    for i in range(tamanho):
        get = aux.elemento
        aux = aux.proximo
        l1.append(get)
    #primeira forma -> função pré definida 
    #print(l1[::-1])
    #segunda forma -> manipulação por for
    l2 = []
    for i in range(tamanho - 1, -1, -1 ):
       get = l1[i]
       l2   .append(get)
    print(l2)

