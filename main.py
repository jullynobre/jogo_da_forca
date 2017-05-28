from tkinter import *
from tkinter.ttk import *
import pickle
import random


class App:
    def __init__(self, root=None):
        array_letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "p",
                        "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        array_buttons = []

        s = Style()

        s.configure('Title.TFrame', background='#00008D')
        s.configure('Container.TFrame')
        s.configure('T.TLabel', background="#00008D", foreground="white", font=("", 35))
        s.configure('D.TLabel', foreground="#00008D", font=("", 15))
        s.configure('D.TEntry', foreground="#00008D")
        s.configure('MenuButtons.TButton', highlightbackground="#C8C4FF", foreground="#00008D", font=("", 15))

        titulo_frame = Frame(root, style='Title.TFrame')
        titulo_frame.place(height=100, width=800)
        titulo_frame.config()

        titulo = Label(titulo_frame, text="JOGO DA FORCA", style='T.TLabel')
        titulo.pack(pady=20)

        main_frame = Frame(root, style='Container.TFrame')
        main_frame.place(height=400, width=800, y=160)
        main_frame.config()

        def novojogo():
            main_frame.destroy()
            frame_iniciar_jogo = Frame(root, style='Container.TFrame')
            frame_iniciar_jogo.place(height=400, width=800, y=160)
            frame_iniciar_jogo.config()

            lbl_nome_jogador = Label(frame_iniciar_jogo, text="Nome do Jogador: ", style='D.TLabel')
            lbl_nome_jogador.pack(pady=20)

            str_nome = StringVar()
            nome_jogador = Entry(frame_iniciar_jogo, style='D.TEntry', font=("", 15), width=30)
            nome_jogador.pack()

            lbl_dificuldade = Label(frame_iniciar_jogo, text="Dificuldade: ", style='D.TLabel')
            lbl_dificuldade.pack(pady=20)

            lista = StringVar(frame_iniciar_jogo)
            lista.set("Fácil")
            dificuldade = OptionMenu(frame_iniciar_jogo, lista, "Fácil", "Fácil", "Médio", "Difícil", style='D.TLabel')
            dificuldade.pack()
            difi = lista.get()

            def iniciar():
<<<<<<< HEAD
                #escolha da palavra
                inputFile = open("palavras.pkl",'rb')
                if(difi == "Fácil"):
                    palavras1 = pickle.load(inputFile)
                    palavra = palavras1[random.randint(0,4)]
                if(difi == "Médio"):
=======
                frame_iniciar_jogo.destroy()

                frame_jogo_left = Frame(root, style='Container.TFrame')
                frame_jogo_left.place(height=400, width=335, x=50, y=150)
                frame_jogo_left.config()

                frame_jogo_right = Frame(root, style='Container.TFrame')
                frame_jogo_right.place(height=400, width=315, x=435, y=150)
                frame_jogo_right.config()

                inputFile = open("palavras.pkl", 'rb')
                if(difi == "Fácil"):
                    palavras1 = pickle.load(inputFile)
                    #palavra = palavras1[random.randint(0,4)]
                elif(difi == "Médio"):
>>>>>>> origin/master
                    palavras2 = pickle.load(inputFile)
                    #palavra = palavras2[random.randint(0,4)]
                elif(difi == "Difícil"):
                    palavras3 = pickle.load(inputFile)
<<<<<<< HEAD
                    palavra = palavras3[random.randint(0,4)]

                #gerador do label que vai representar a palavra
                x = "_"
                y = " _"
                for i in range(len(palavra)-1):
                    x+=y
                print (palavra)
                print (x)
                
                
                
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
                frame_iniciar_jogo.destroy()
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
                contBai20 = Frame(height=10,width=700)
                contBai20.pack(side="bottom")
                contEsq20 = Frame(height=500,width=400)
                contEsq20.pack(side="left")
                contDir20 = Frame(height=100,width=400)
                contDir20.pack(side="bottom")
##                #Traços
##                for i in range(len(palavra)):
##                    quantostracos += 1
##                tracos = Label(text)
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
                #Forc
                forca = PhotoImage(file="forca0.png")
                label20 = Label(contEsq20, image=forca)
                label20.pack(side="left")

                
=======
                    #palavra = palavras3[random.randint(0,4)]

                def jogar_letra(letra):
                    index = array_letras.index(letra)
                    array_buttons[index].state(["disabled"])
                    print(letra)

                frame1 = Frame(frame_jogo_right)
                frame1.place(height=380, width=75, x=0)
                frame1.config()
                frame2 = Frame(frame_jogo_right)
                frame2.place(height=380, width=75, x=80)
                frame2.config()
                frame3 = Frame(frame_jogo_right)
                frame3.place(height=380, width=75, x=160)
                frame3.config()
                frame4 = Frame(frame_jogo_right)
                frame4.place(height=380, width=75, x=240)
                frame4.config()

                x = 1
                for i in range(26):
                    if x == 1:
                        array_buttons.append(Button(frame1, text=array_letras[i],
                                                    command=lambda name=i: jogar_letra(array_letras[name])))
                        array_buttons[i].pack(pady=10)
                    elif x == 2:
                        array_buttons.append(Button(frame2, text=array_letras[i],
                                                    command=lambda name=i: jogar_letra(array_letras[name])))
                        array_buttons[i].pack(pady=10)
                    elif x == 3:
                        array_buttons.append(Button(frame3, text=array_letras[i],
                                                    command=lambda name=i: jogar_letra(array_letras[name])))
                        array_buttons[i].pack(pady=10)
                    elif x == 4:
                        array_buttons.append(Button(frame4, text=array_letras[i],
                                                    command=lambda name=i: jogar_letra(array_letras[name])))
                        array_buttons[i].pack(pady=10)
                        x = 0
                    x += 1
>>>>>>> origin/master

            def voltar():
                root.destroy()
                newroot = Tk()
                newroot.geometry("800x600+50+50")
                App(newroot)
                newroot.mainloop()

            iniciar = Button(frame_iniciar_jogo, text="Iniciar", style='MenuButtons.TButton', command=iniciar)
            iniciar.pack(pady=50)
            voltar = Button(frame_iniciar_jogo, text="Voltar", style='MenuButtons.TButton', command=voltar)
            voltar.pack()

        novo_jogo = Button(main_frame, text="        Novo Jogo       ", style='MenuButtons.TButton', command=novojogo)
        novo_jogo.pack(pady=20)
        continuar_jogo = Button(main_frame, text="     Continuar Jogo    ", style='MenuButtons.TButton')
        continuar_jogo.pack(pady=20)
        placares_jogo = Button(main_frame, text="         Placares         ", style='MenuButtons.TButton')
        placares_jogo.pack(pady=20)
        gerenciar_palavras = Button(main_frame, text="  Gerenciar Palavras ", style='MenuButtons.TButton')
        gerenciar_palavras.pack(pady=20)

root = Tk()
root.geometry("800x600+50+50")
App(root)
root.mainloop()
