from tkinter import *
from tkinter import ttk
import pickle
import random

#-----------------------------Configuração da janela---------------------------#
#definição da classes
class App(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

#Inicializa um objeto nos moldes da classe App
myapp = App()
#Seta o Titulo do objeto App
myapp.master.title("Jogo da Forca")
#Seta maximo e minimo do tamanho
myapp.master.maxsize(800,600)
myapp.master.minsize(800,600)


#----------------------------------Submenus------------------------------------#
def jogo():
    #Limpeza da tela
    contTop1.destroy()
    bordEsq1.destroy()
    Menu1.destroy()
    bordDir1.destroy()
    esp10.destroy()
    esp11.destroy()
    esp12.destroy()
    esp13.destroy()
    


def NovoJogo():
    def jogo():
        inputFile = open("palavras.pkl",'rb')
        if(dificuldade == "Fácil"):
            palavras1 = pickle.load(inputFile)
            palavra = palavras1[random.randint(0,4)]
        if(dificuldade == "Médio"):
            palavras2 = pickle.load(inputFile)
            palavra = palavras2[random.randint(0,4)]
        if(dificuldade == "Difícil"):
            palavras3 = pickle.load(inputFile)
            palavra = palavras3[random.randint(0,4)]

        
        
        
        def letraA():
            print("X")
        def letraB():
            print("X")
        def letraC():
            print("X")
        def letraD():
            print("X")
        def letraE():
            print("X")
        def letraF():
            print("X")
        def letraG():
            print("X")
        def letraH():
            print("X")
        def letraI():
            print("X")
        def letraJ():
            print("X")
        def letraK():
            print("X")
        def letraL():
            print("X")
        def letraM():
            print("X")
        def letraN():
            print("X")
        def letraO():
            print("X")
        def letraP():
            print("X")
        def letraQ():
            print("X")
        def letraR():
            print("X")
        def letraS():
            print("X")
        def letraT():
            print("X")
        def letraU():
            print("X")
        def letraV():
            print("X")
        def letraW():
            print("X")
        def letraX():
            print("X")
        def letraY():
            print("X")
        def letraZ():
            print("X")
        
        #Limpeza da tela
        contTop1.destroy()
        bordEsq1.destroy()
        Menu1.destroy()
        bordDir1.destroy()
        esp10.destroy()
        esp11.destroy()
        esp12.destroy()
        esp13.destroy()
        #Espaçamentos
        bord200 = Frame(width=5)
        bord201 = Frame(width=5)
        bord202 = Frame(width=5)
        bord203 = Frame(width=5)
        bord204 = Frame(width=5)
        bord205 = Frame(width=5)
        bord206 = Frame(width=5)
        bord207 = Frame(width=5)
        bord208 = Frame(width=5)
        bord209 = Frame(width=5)
        bord2010 = Frame(width=5)
        bord2011 = Frame(width=5)
        bord2012 = Frame(width=5)
        bord2013 = Frame(width=5)
        bord2014 = Frame(width=5)
        bord2015 = Frame(width=5)
        bord2016 = Frame(width=5)
        bord2017 = Frame(width=5)
        bord2018 = Frame(width=5)
        bord2019 = Frame(width=5)
        bord2020 = Frame(width=5)
        bord2021 = Frame(width=5)
        bord2022 = Frame(width=5)
        bord2023 = Frame(width=5)
        bord2024 = Frame(width=5)
        bord2025 = Frame(width=5)
        #Frames
        borBai20 = Frame(height=25,width=800)
        borBai20.pack(side="bottom")
        contBai20 = Frame(height=10,width=700,bg="lightgray")
        contBai20.pack(side="bottom")
        contEsq20 = Frame(height=500,width=400)
        contEsq20.pack(side="left")
        contDir20 = Frame(height=100,width=400,bg="red")
        contDir20.pack(side="bottom")
        #botões
        A = Button(contBai20,text="A",command=letraA)
        A.pack(side="left")
        bord201.pack(side="left")
        B = Button(contBai20,text="B",command=letraB)
        B.pack(side="left")
        bord202.pack(side="left")
        C = Button(contBai20,text="C",command=letraC)
        C.pack(side="left")
        bord203.pack(side="left")
        D = Button(contBai20,text="D",command=letraD)
        D.pack(side="left")
        bord203.pack(side="left")
        E = Button(contBai20,text="E",command=letraE)
        E.pack(side="left")
        bord204.pack(side="left")
        F = Button(contBai20,text="F",command=letraF)
        F.pack(side="left")
        bord205.pack(side="left")
        G = Button(contBai20,text="G",command=letraG)
        G.pack(side="left")
        bord206.pack(side="left")
        H = Button(contBai20,text="H",command=letraH)
        H.pack(side="left")
        bord207.pack(side="left")
        I = Button(contBai20,text="I",command=letraI)
        I.pack(side="left")
        bord208.pack(side="left")
        J = Button(contBai20,text="J",command=letraJ)
        J.pack(side="left")
        bord209.pack(side="left")
        K = Button(contBai20,text="K",command=letraK)
        K.pack(side="left")
        bord2010.pack(side="left")
        L = Button(contBai20,text="L",command=letraL)
        L.pack(side="left")
        bord2011.pack(side="left")
        M = Button(contBai20,text="M",command=letraM)
        M.pack(side="left")
        bord2012.pack(side="left")
        N = Button(contBai20,text="N",command=letraN)
        N.pack(side="left")
        bord2013.pack(side="left")
        O = Button(contBai20,text="O",command=letraO)
        O.pack(side="left")
        bord2014.pack(side="left")
        P = Button(contBai20,text="P",command=letraP)
        P.pack(side="left")
        bord2015.pack(side="left")
        Q = Button(contBai20,text="Q",command=letraQ)
        Q.pack(side="left")
        bord2016.pack(side="left")
        R = Button(contBai20,text="R",command=letraR)
        R.pack(side="left")
        bord2017.pack(side="left")
        S = Button(contBai20,text="S",command=letraS)
        S.pack(side="left")
        bord2018.pack(side="left")
        T = Button(contBai20,text="T",command=letraT)
        T.pack(side="left")
        bord2019.pack(side="left")
        U = Button(contBai20,text="U",command=letraU)
        U.pack(side="left")
        bord2020.pack(side="left")
        V = Button(contBai20,text="V",command=letraV)
        V.pack(side="left")
        bord2021.pack(side="left")
        W = Button(contBai20,text="W",command=letraW)
        W.pack(side="left")
        bord2022.pack(side="left")
        X = Button(contBai20,text="X",command=letraX)
        X.pack(side="left")
        bord2023.pack(side="left")
        Y = Button(contBai20,text="Y",command=letraY)
        Y.pack(side="left")
        bord2024.pack(side="left")
        Z = Button(contBai20,text="Z",command=letraZ)
        Z.pack(side="left")
        #Forca
        label20 = Label(contEsq20, image=forca)
        label20.pack(side="left")
        
        
    
    #Limpeza da tela
    contTop.destroy()
    bordEsq.destroy()
    Menus.destroy()
    bordDir.destroy()
    esp0.destroy()
    esp1.destroy()
    esp2.destroy()
    esp3.destroy()
    #Novos Frames
    contTop1 = Frame(height=175,width=800,bg="lightgray")
    bordEsq1 = Frame(height=425,width=350,bg="lightgray")
    Menu1 = Frame(height=425,width=350,bg="lightgray")
    bordDir1 = Frame(height=425,width=350,bg="lightgray")
    contTop1.pack(side="top")
    bordEsq1.pack(side="left")
    Menu1.pack(side="left")
    bordDir1.pack(side="left")
    #Espaçamentos
    esp11 = Frame(Menu1,height=25,bg="lightgray")
    esp10 = Frame(Menu1,height=146,bg="lightgray")
    esp12 = Frame(Menu1,height=25,bg="lightgray")
    esp13 = Frame(Menu1,height=110,bg="lightgray")
    #imagem
    label10 = Label(contTop1, image=foto)
    label10.pack()
    #Labels
    label11 = Label(Menu1,text="Nome do Jogador",bg="lightgray")
    label12 = Label(Menu1,text="Dificuldade",bg="lightgray")
    #Entrada de Texto
    jogador1 = Entry(Menu1)
    #Lista de Dificuldades
    lista = StringVar(Menu1)
    lista.set("Fácil")
    w = OptionMenu(Menu1, lista, "Fácil", "Médio", "Difícil")
    #Botão
    Iniciar11 = Button(Menu1,text="Iniciar",command=jogo)
    #Setando os elementos do frame central
    esp10.pack()
    label11.pack()
    jogador1.pack()
    esp11.pack()
    label12.pack()
    w.pack()
    esp12.pack()
    Iniciar11.pack()
    esp13.pack()
    nome = jogador1.get()
    dificuldade = lista.get()

    
    

    
#--------------------------------Menu Principal--------------------------------#
#frames(onde põe os widgets)
contTop = Frame(height=175,width=800,bg="blue")
bordEsq = Frame(height=425,width=350,bg="lightgray")
Menus = Frame(height=425,width=350,bg="lightgray")
bordDir = Frame(height=425,width=350,bg="lightgray")
contTop.pack(side="top")
bordEsq.pack(side="left")
Menus.pack(side="left")
bordDir.pack(side="left")
#imagem
foto = PhotoImage(file="titulo.png")
forca = PhotoImage(file="forca0.png")
label = Label(contTop, image=foto)
label.pack()
#Espaçamentos
esp0 = Frame(Menus,height=146,bg="lightgray")
esp1 = Frame(Menus,height=25,bg="lightgray")
esp2 = Frame(Menus,height=25,bg="lightgray")
esp3 = Frame(Menus,height=151,bg="lightgray")
#Botões
novo = Button(Menus,text="Iniciar Novo Jogo",command=NovoJogo)
cont = Button(Menus,text="Continuar Jogo")
plac = Button(Menus,text="Placares")
#Setando os elementos do frame central
esp0.pack()
novo.pack()
esp1.pack()
cont.pack()
esp2.pack()
plac.pack()
esp3.pack()








myapp.mainloop()
