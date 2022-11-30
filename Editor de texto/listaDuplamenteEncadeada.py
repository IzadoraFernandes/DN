class No: #criação da classe no 
    def __init__(self, caractere):
        self.anterior = None
        self.proximo = None
        self.caractere = caractere
class ListaDuplamenteEncadeada: #criação da lista duplamente encadeada 
    def __init__(self):
        self.marcador = No("*") #saber onde está o cursou para saber onde adicionar e remover
        self.primeiro = None # cabeça da lista, caso queira pegar o primeiro elemento
        self.ultimo = None #cauda da lista.
    def mostrar(self):
        x = self.primeiro #vai percerrer a lista e imprimir os caracteres 
        while x != None: #se ainda não chegou au final.......
            if(x.caractere == 'enter'): #descer uma linha na linha
                print(" ")
            elif(x.caractere == 'space' ): # da um espaço dentro da lista
                print(" ",end="")
            elif(x.caractere == "shift" or x.caractere == 'right shift'): #inserir uma letra maiuscula e não inserir o shift
                pass
            else:  
                print( x.caractere, end="") # so vai printar ao lado, para formar "uma única" palavra .
            x = x.proximo #pulano os nos ate ao final
    def createNo(self, caractere): #criando o no com o caractere que foi passado.
        novoNo = No(caractere)
        
        if(self.marcador.anterior == None and self.marcador.proximo != None): #0*1234  caso adicione alguma coisa no inicio da lista.
            self.primeiro.anterior = novoNo #  o que era primeiro agora tem um anterior 
            self.marcador.proximo = self.primeiro # aponta para o que era o primeiro elemento
            self.marcador.anterior = novoNo # aponta para o novo elemento inserido 
            novoNo.proximo = self.primeiro # o primeiro elemento inserido, aponta para o seu secessor.
            self.primeiro = novoNo # primeiro elemento é a cabeça da lista
            
        elif(self.marcador.anterior == None and self.marcador.proximo == None):#nenhum elemeno na lista, 1
            self.primeiro = novoNo
            self.ultimo = novoNo
            self.marcador.anterior = novoNo
            
        elif(self.marcador.proximo == None and self.marcador.anterior != None):#contrario 1234*5=> none. isso acontece quando já tem um anterior, caso contrario, entraria na função de cima
            self.ultimo.proximo = novoNo
            self.marcador.anterior = novoNo
            novoNo.anterior = self.ultimo
            self.ultimo = novoNo
            
        else:#inserir no meio 
            anterior = self.marcador.anterior
            anterior.proximo = novoNo
            novoNo.proximo = self.marcador.proximo
            novoNo.anterior = anterior
            self.marcador.anterior = novoNo
            return


    def remove(self): #remove algum caracter que foi inserido na lista
        if(self.marcador.anterior):
            
            if(self.marcador.anterior.anterior == None and self.marcador.proximo != None):#23
                proximo = self.marcador.proximo 
                self.primeiro = proximo
                proximo.anterior = None
                self.marcador.anterior = None
                
            elif(self.marcador.anterior.anterior == None):
                self.marcador.anterior = None
                self.marcador.proximo = self.primeiro.proximo
                self.primeiro = self.primeiro.proximo
                
            elif(self.marcador.proximo == None and self.marcador.anterior != None):#125*83
                anterior = self.marcador.anterior.anterior
                anterior.proximo = None
                self.marcador.anterior = anterior
                self.ultimo = anterior
                
            else:#123*4
                anterior = self.marcador.anterior.anterior
                proximo = self.marcador.proximo
                self.marcador.anterior = anterior
                proximo.anterior = anterior
                anterior.proximo = proximo
            
    
    
    def moveMarcador(self, type): # movimentar o marcador(mouse) na lista de acordo com a direção.
        
        if(type == 'left'):
            if(self.marcador.anterior):
                
                if(self.marcador.anterior == self.primeiro):#125*473
                    
                    
                    self.marcador.anterior = None
                    self.marcador.proximo = self.primeiro
                else:
                    
                    proximo = self.marcador.anterior # ex: 1234*, o anterior do aponador é 4, quando apertar <= então o anerior dele se torna o posterior, e agora seu anterior é o 123*4.
                    anterior = self.marcador.anterior.anterior #ex: o apontador quando esta na ultima posição, o seu anterior será  o anterior dele 2x.
                    self.marcador.anterior = anterior # o novo anterior sera o antigo anterior do anterior dele e agora o proximo agora será o 4 . ex: 1234* agora sera 123*4 o que o ponteiro irá apresentar
                    self.marcador.proximo = proximo #ex: 123*4 se aperar => será 1234* e o proximo será none.
                    
            
        if(type == 'right'):
            
            if(self.marcador.proximo):
                
                if(self.marcador.proximo == self.ultimo):
                    
                    self.marcador.anterior = self.ultimo
                    self.marcador.proximo = None
                else: #123*4
                    anterior = self.marcador.proximo
                    proximo = self.marcador.proximo.proximo
                    self.marcador.anterior = anterior 
                    self.marcador.proximo = proximo
                    
                    
            
            
        
        
            
            


  
        
            
            
