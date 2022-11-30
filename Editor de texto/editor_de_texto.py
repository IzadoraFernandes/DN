from tkinter import *

import keyboard

from listaDuplamenteEncadeada import *

lista = ListaDuplamenteEncadeada()



class Editor:
        
    def __init__(self, master=None): #cria um dicionaio para ignorar os caracteres abaixo
        caracteresEspecias={
            #Ignorar
            'up': '',
            'down':'',
            'right': '',
            'left':'',
            
            
            'alt':'',
            'ctrl':'',
            'left windows': '',
            'alt gr': '',
            'menu': '',
            'caps': '',
            'locktab': '',  
            'decimal':'', 
            'backspace': '',  
        }
        
        master.title("Editor de texto")  #nome da janela do editor de texto
        master.geometry("1280x720+300+140")  #tamanho e local onde as informaçõe vão aparecer
        
        frameInput = Frame(master, bg="#85B777") # tamanho da tela de input 
        frameInput.place(width=1280, height=720, x=0, y=0)
        inputText = Text(frameInput, width=1280, font=("Arial", 20), height=720, x=0, y=0)
        inputText.pack()
        

        def press(key): #para recebr os dados  enviar para a lista duplamene encadeada 
            if(key.name not in caracteresEspecias): #serve para veriicar se a informação digitada esta nos caracteres especiais, caso não esteja irá criar um no do elemeno digitado.
                lista.createNo(key.name)
            elif(key.name == 'left' or key.name == 'right'): # verificador de onde o cursou esá para adicionar um novo elemento d local onde está o mouse.
                lista.moveMarcador(key.name)
            elif(key.name == 'backspace'): #funçao para remover o caracter onde está o cursou. 
                lista.remove()
        
            
            
            
        keyboard.on_press(press) #função para lê a ação do teclado e percorrer a função acima.
        

root = Tk()
Editor(root)
root.mainloop()
lista.mostrar()
