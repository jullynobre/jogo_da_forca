from tkinter import *
from tkinter.ttk import *
import pickle
import random


class App:
    def __init__(self, root=None):
        array_letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                        "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        array_buttons = []
        entry_letras = []
        array_forcas = [1, 2, 3, 4, 5, 6, 7]
        completo = []
        erros = 0
        acertos = 0

        s = Style()

        s.configure('Title.TFrame', background='#00008D')
        s.configure('Plac.TFrame', background='#FFFFFF')
        s.configure('Container.TFrame')
        s.configure('T.TLabel', background="#00008D", foreground="white", font=("", 35))
        s.configure('GO.TLabel', background="#00008D", foreground="white")
        s.configure('D.TLabel', foreground="#00008D", font=("", 15))
        s.configure('D.TEntry', foreground="#00008D")
        s.configure('MenuButtons.TButton', highlightbackground="#C8C4FF", foreground="#00008D", font=("", 15))
        s.configure('words.TButton', highlightbackground="#C8C4FF", foreground="#00008D", font=("", 10))

        titulo_frame = Frame(root, style='Title.TFrame')
        titulo_frame.place(height=100, width=800)
        titulo_frame.config()

        titulo = Label(titulo_frame, text="JOGO DA FORCA", style='T.TLabel')
        titulo.pack(pady=20)

        main_frame = Frame(root, style='Container.TFrame')
        main_frame.place(height=400, width=800, y=160)
        main_frame.config()


        def contjogo():
            main_frame.destroy()
            
            inputFile = open("save.pkl", 'rb')
                        
            difi = pickle.load(inputFile)
            nome2 = pickle.load(inputFile)
            pontos = pickle.load(inputFile)
            dPontos = pickle.load(inputFile)
            erros = pickle.load(inputFile)
            palavra = pickle.load(inputFile)
            palavra_auxiliar = pickle.load(inputFile)
            ativadas = pickle.load(inputFile)
                        
            inputFile.close()
            palavra_auxiliar = list(palavra_auxiliar)
            ativadas = list(ativadas)
            print(palavra)


            frame_jogo_left = Frame(root, style='Container.TFrame')
            frame_jogo_left.place(height=400, width=335, x=50, y=150)
            frame_jogo_left.config()

            frame_jogo_right = Frame(root, style='Container.TFrame')
            frame_jogo_right.place(height=400, width=315, x=435, y=150)
            frame_jogo_right.config()


            #gerador do label que vai representar a palavra
            tracosX = "_"
            y = "_"
            for i in range(len(palavra)-1):
                tracosX += y

            frame_tracos = Frame(frame_jogo_left)
            frame_tracos.place(height=30, width=315, x=10)
            frame_tracos.pack(side="bottom")

            for i in range(len(palavra)):
                entry_letras.append(Entry(frame_tracos, style='D.TEntry', font=("", 20), width=2))
                entry_letras[i].pack(side='left', padx=5)
                entry_letras[i].state(["disabled"])

            i = 1
            while i < 8:
                image = PhotoImage(file=("Imagens\\forca0" + str(i) + ".png"))
                array_forcas[(i - 1)] = Label(frame_jogo_left, image=image)
                array_forcas[(i - 1)].image = image
                i += 1


            array_forcas[erros].pack()


            def jogar_letra(letra):
                index = array_letras.index(letra)
                array_buttons[index].state(["disabled"])


                inputFile = open("save.pkl", 'rb')
                        
                difi = pickle.load(inputFile)
                nome2 = pickle.load(inputFile)
                pontos = pickle.load(inputFile)
                dPontos = pickle.load(inputFile)
                erros = pickle.load(inputFile)
                palavra = pickle.load(inputFile)
                palavra_auxiliar = pickle.load(inputFile)
                ativadas = pickle.load(inputFile)
                        
                inputFile.close()
                ativadas = list(ativadas)
                palavra_auxiliar = list(palavra_auxiliar)
                    
                if palavra.count(letra) == 0:
                        
                        
                    pontos = str(int(pontos) - int(dPontos))
                    if erros < 6:
                        array_forcas[erros].destroy()
                        erros += 1
                        array_forcas[erros].pack()
                    else:
                        inputFile = open("ranking.pkl", 'rb')
                            
                        jog = pickle.load(inputFile)
                        pon = pickle.load(inputFile)
                            
                        inputFile.close()

                        if (int(pontos) - int(pon[4])) > 0:
                            if (int(pontos) - int(pon[3])) > 0:
                                if (int(pontos) - int(pon[2])) > 0:
                                    if (int(pontos) - int(pon[1])) > 0:
                                        if (int(pontos) - int(pon[0])) > 0:
                                            jog[4] = jog[3]
                                            pon[4] = pon[3]
                                            jog[3] = jog[2]
                                            pon[3] = pon[2]
                                            jog[2] = jog[1]
                                            pon[2] = pon[1]
                                            jog[1] = jog[0]
                                            pon[1] = pon[0]
                                            jog[0] = nome2
                                            pon[0] = pontos
                                        else:
                                            jog[5] = jog[4]
                                            pon[5] = pon[4]
                                            jog[4] = jog[3]
                                            pon[4] = pon[3]
                                            jog[3] = jog[2]
                                            pon[3] = pon[2]
                                            jog[2] = nome2
                                            pon[2] = pontos
                                    else:
                                        jog[4] = jog[3]
                                        pon[4] = pon[3]
                                        jog[3] = jog[2]
                                        pon[3] = pon[2]
                                        jog[2] = nome2
                                        pon[2] = pontos
                                else:
                                    jog[4] = jog[3]
                                    pon[4] = pon[3]
                                    jog[3] = nome2
                                    pon[3] = pontos
                            else:
                                jog[4] = nome2
                                pon[4] = pontos
                        else:
                            print("troxa")
                        
                        output = open("ranking.pkl",'wb')
                        
                        pickle.dump(jog, output)
                        pickle.dump(pon, output)

                        output.close()
                            
                        frame_jogo_left.destroy()
                        frame_jogo_right.destroy()
                        titulo_frame.destroy()

                        frame_game_over = Frame(root, style='Title.TFrame')
                        frame_game_over.place(height=600, width=800, x=0, y=0)
                        frame_game_over.config()

                        image_game_over = PhotoImage(file="Imagens\\gameover.png")
                        label_game_over = Label(frame_game_over, image=image_game_over, style='GO.TLabel')
                        label_game_over.image = image_game_over
                        label_game_over.pack(padx=215, pady=20)

                        label_pontuacao = Label(frame_game_over, text=("Pontuação: " + str(pontos)),
                                                style='GO.TLabel', font=("", 30))
                        label_pontuacao.pack()

                        def voltar2():
                            root.destroy()
                            newroot = Tk()
                            newroot.geometry("800x600+50+50")
                            App(newroot)
                            newroot.mainloop()

                        voltar2 = Button(frame_game_over, text="Voltar", style='MenuButtons.TButton',
                                        command=voltar2)
                        voltar2.pack(pady=20)

                    output = open("save.pkl", 'wb')
                        
                    pickle.dump(difi, output)
                    pickle.dump(nome2, output)
                    pickle.dump(pontos, output)
                    pickle.dump(dPontos, output)
                    pickle.dump(erros, output)
                    pickle.dump(palavra, output)
                    pickle.dump(palavra_auxiliar, output)
                    pickle.dump(ativadas, output)
                        
                    output.close()
                else:
                    inputFile = open("save.pkl", 'rb')
                        
                    difi = pickle.load(inputFile)
                    nome2 = pickle.load(inputFile)
                    pontos = pickle.load(inputFile)
                    dPontos = pickle.load(inputFile)
                    erros = pickle.load(inputFile)
                    palavra_auxiliar = pickle.load(inputFile)
                    ativadas = pickle.load(inputFile)
                        
                    inputFile.close()
                    palavra_auxiliar = list(palavra_auxiliar)
                    ativadas = list(ativadas)

                    while palavra_auxiliar.count(letra) > 0:
                        index = palavra_auxiliar.index(letra)
                        palavra_auxiliar[index] = "-"

                        pontos = str(int(pontos)+100)

                        entry_letras[index].state(["!disabled"])
                        entry_letras[index].insert(0, letra)
                        entry_letras[index].state(["disabled"])
                        completo.append("-")
                            
                    output = open("save.pkl",'wb')

                    pickle.dump(difi, output)
                    pickle.dump(nome2, output)
                    pickle.dump(pontos, output)
                    pickle.dump(dPontos, output)
                    pickle.dump(erros, output)
                    pickle.dump(palavra, output)
                    pickle.dump(palavra_auxiliar, output)
                    pickle.dump(ativadas, output)

                    output.close()


                    if len(completo) == len(palavra_auxiliar):
                        inputFile = open("ranking.pkl", 'rb')
                            
                        jog = pickle.load(inputFile)
                        pon = pickle.load(inputFile)
                            
                        inputFile.close()

                        if (int(pontos) - pon[4]) > 0:
                            if (int(pontos) - pon[3]) > 0:
                                if (int(pontos) - pon[2]) > 0:
                                    if (int(pontos) - pon[1]) > 0:
                                        if (int(pontos) - pon[0]) > 0:
                                            jog[4] = jog[3]
                                            pon[4] = pon[3]
                                            jog[3] = jog[2]
                                            pon[3] = pon[2]
                                            jog[2] = jog[1]
                                            pon[2] = pon[1]
                                            jog[1] = jog[0]
                                            pon[1] = pon[0]
                                            jog[0] = nome2
                                            pon[0] = pontos
                                        else:
                                            jog[5] = jog[4]
                                            pon[5] = pon[4]
                                            jog[4] = jog[3]
                                            pon[4] = pon[3]
                                            jog[3] = jog[2]
                                            pon[3] = pon[2]
                                            jog[2] = nome2
                                            pon[2] = pontos
                                    else:
                                        jog[4] = jog[3]
                                        pon[4] = pon[3]
                                        jog[3] = jog[2]
                                        pon[3] = pon[2]
                                        jog[2] = nome2
                                        pon[2] = pontos
                                else:
                                    jog[4] = jog[3]
                                    pon[4] = pon[3]
                                    jog[3] = nome2
                                    pon[3] = pontos
                            else:
                                jog[4] = nome2
                                pon[4] = pontos
                        else:
                            print("troxa")
                            
                        output = open("ranking.pkl",'wb')

                        pickle.dump(jog, output)
                        pickle.dump(pon, output)

                        output.close()

                            
                        frame_jogo_left.destroy()
                        frame_jogo_right.destroy()
                        titulo_frame.destroy()

                        frame_congra = Frame(root, style='Plac.TFrame')
                        frame_congra.place(height=600, width=800, x=0, y=0)
                        frame_congra.config()

                        image_cong = PhotoImage(file="Imagens\\congratulations.png")

                        lp = Label(frame_congra, image=image_cong)
                        lp.image = image_cong
                        lp.pack(side="top")
                        lp = Label(frame_congra, text=("Pontuação: " + pontos), font=("", 30))
                        lp.pack(pady=50)

                        def voltar():
                            root.destroy()
                            newroot = Tk()
                            newroot.geometry("800x600+50+50")
                            App(newroot)
                            newroot.mainloop()

                        voltar = Button(frame_congra, text="Voltar", style='MenuButtons.TButton',
                                        command=voltar)
                        voltar.pack()

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
                        array_buttons.append(Button(frame1, text=array_letras[i], style='words.TButton',
                                                    command=lambda name=i: jogar_letra(array_letras[name])))
                        array_buttons[i].pack(pady=10)
                    elif x == 2:
                        array_buttons.append(Button(frame2, text=array_letras[i], style='words.TButton',
                                                    command=lambda name=i: jogar_letra(array_letras[name])))
                        array_buttons[i].pack(pady=10)
                    elif x == 3:
                        array_buttons.append(Button(frame3, text=array_letras[i], style='words.TButton',
                                                    command=lambda name=i: jogar_letra(array_letras[name])))
                        array_buttons[i].pack(pady=10)
                    elif x == 4:
                        array_buttons.append(Button(frame4, text=array_letras[i], style='words.TButton',
                                                    command=lambda name=i: jogar_letra(array_letras[name])))
                        array_buttons[i].pack(pady=10)
                        x = 0
                    x += 1




        
        def novojogo():
            main_frame.destroy()
            frame_iniciar_jogo = Frame(root, style='Container.TFrame')
            frame_iniciar_jogo.place(height=400, width=800, y=160)
            frame_iniciar_jogo.config()

            lbl_nome_jogador = Label(frame_iniciar_jogo, text="Nome do Jogador: ", style='D.TLabel')
            lbl_nome_jogador.pack(pady=20)

            nome = StringVar()
            nome.trace("w", lambda name, index, mode, nome=nome: callback(nome))
            nome_jogador = Entry(frame_iniciar_jogo, style='D.TEntry', font=("", 15), width=30,
                                 textvariable=nome)
            nome_jogador.pack()
            lbl_dificuldade = Label(frame_iniciar_jogo, text="Dificuldade: ", style='D.TLabel')
            lbl_dificuldade.pack(pady=20)

            lista = StringVar(frame_iniciar_jogo)
            lista.set("Fácil")
            dificuldade = OptionMenu(frame_iniciar_jogo, lista, "Fácil", "Fácil", "Médio", "Difícil", style='D.TLabel')
            dificuldade.pack()


            def iniciar():
##                difi = lista.get()
                nome2 = nome_jogador.get()
                frame_iniciar_jogo.destroy()

                frame_jogo_left = Frame(root, style='Container.TFrame')
                frame_jogo_left.place(height=400, width=335, x=50, y=150)
                frame_jogo_left.config()

                frame_jogo_right = Frame(root, style='Container.TFrame')
                frame_jogo_right.place(height=400, width=315, x=435, y=150)
                frame_jogo_right.config()

                palavra = ""
                #escolha da palavra
                inputFile = open("palavras.pkl", 'rb')
                if (difi == "Fácil"):
                    palavras1 = pickle.load(inputFile)
                    palavra = palavras1[random.randint(0,4)]
                    pontos = 1000
                    dPontos = 20
                elif (difi == "Médio"):
                    palavras2 = pickle.load(inputFile)
                    palavra = palavras2[random.randint(0,4)]
                    pontos = 2000
                    dPontos = 50
                elif (difi == "Difícil"):
                    palavras3 = pickle.load(inputFile)
                    palavra = palavras3[random.randint(0, 4)]
                    pontos = 3000
                    dPontos = 100

                palavra = palavra.upper()
                print(palavra)
                
                palavra_auxiliar = list(palavra)
                print(palavra_auxiliar)
                erros = 0
                ativadas = []
                
                output = open("save.pkl",'wb')

                pickle.dump(difi, output)
                pickle.dump(nome2, output)
                pickle.dump(pontos, output)
                pickle.dump(dPontos, output)
                pickle.dump(erros, output)
                pickle.dump(palavra, output)
                pickle.dump(palavra_auxiliar, output)
                pickle.dump(ativadas, output)

                output.close()

                #gerador do label que vai representar a palavra
                tracosX = "_"
                y = "_"
                for i in range(len(palavra)-1):
                    tracosX += y

                frame_tracos = Frame(frame_jogo_left)
                frame_tracos.place(height=30, width=315, x=10)
                frame_tracos.pack(side="bottom")

                for i in range(len(palavra)):
                    entry_letras.append(Entry(frame_tracos, style='D.TEntry', font=("", 20), width=2))
                    entry_letras[i].pack(side='left', padx=5)
                    entry_letras[i].state(["disabled"])

                i = 1
                while i < 8:
                    image = PhotoImage(file=("Imagens\\forca0" + str(i) + ".png"))
                    array_forcas[(i - 1)] = Label(frame_jogo_left, image=image)
                    array_forcas[(i - 1)].image = image
                    i += 1

                array_forcas[0].pack()


                

                def callback(nome):
                    if nome.get() != "":
                        iniciar.state(["!disabled"])
                    else:
                        iniciar.state(["disabled"])

                nome = StringVar()
                nome.trace("w", lambda name, index, mode, nome=nome: callback(nome))
                nome_jogador = Entry(frame_iniciar_jogo, style='D.TEntry', font=("", 15), width=30,
                                     textvariable=nome)
                nome_jogador.pack()
                lbl_dificuldade = Label(frame_iniciar_jogo, text="Dificuldade: ", style='D.TLabel')
                lbl_dificuldade.pack(pady=20)

                lista = StringVar(frame_iniciar_jogo)
                lista.set("Fácil")
                dificuldade = OptionMenu(frame_iniciar_jogo, lista, "Fácil", "Fácil", "Médio", "Difícil", style='D.TLabel')
                dificuldade.pack()

                

                def jogar_letra(letra):
                    inputFile = open("save.pkl", 'rb')
                        
                    difi = pickle.load(inputFile)
                    nome2 = pickle.load(inputFile)
                    pontos = pickle.load(inputFile)
                    dPontos = pickle.load(inputFile)
                    erros = pickle.load(inputFile)
                    palavra = pickle.load(inputFile)
                    palavra_auxiliar = pickle.load(inputFile)
                    ativadas = pickle.load(inputFile)
                        
                    inputFile.close()
                    palavra_auxiliar = list(palavra_auxiliar)
                    ativadas = list(ativadas)
                    ativadas.append(letra)

                    index = array_letras.index(letra)
                    array_buttons[index].state(["disabled"])
                    
                    if palavra.count(letra) == 0:
                        
                        
                        pontos = str(int(pontos) - int(dPontos))
                        if erros < 6:
                            array_forcas[erros].destroy()
                            erros += 1
                            array_forcas[erros].pack()
                        else:
                            inputFile = open("ranking.pkl", 'rb')
                            
                            jog = pickle.load(inputFile)
                            pon = pickle.load(inputFile)
                            
                            inputFile.close()

                            if (int(pontos) - int(pon[4])) > 0:
                                if (int(pontos) - int(pon[3])) > 0:
                                    if (int(pontos) - int(pon[2])) > 0:
                                        if (int(pontos) - int(pon[1])) > 0:
                                            if (int(pontos) - int(pon[0])) > 0:
                                                jog[4] = jog[3]
                                                pon[4] = pon[3]
                                                jog[3] = jog[2]
                                                pon[3] = pon[2]
                                                jog[2] = jog[1]
                                                pon[2] = pon[1]
                                                jog[1] = jog[0]
                                                pon[1] = pon[0]
                                                jog[0] = nome2
                                                pon[0] = pontos
                                            else:
                                                jog[5] = jog[4]
                                                pon[5] = pon[4]
                                                jog[4] = jog[3]
                                                pon[4] = pon[3]
                                                jog[3] = jog[2]
                                                pon[3] = pon[2]
                                                jog[2] = nome2
                                                pon[2] = pontos
                                        else:
                                            jog[4] = jog[3]
                                            pon[4] = pon[3]
                                            jog[3] = jog[2]
                                            pon[3] = pon[2]
                                            jog[2] = nome2
                                            pon[2] = pontos
                                    else:
                                        jog[4] = jog[3]
                                        pon[4] = pon[3]
                                        jog[3] = nome2
                                        pon[3] = pontos
                                else:
                                    jog[4] = nome2
                                    pon[4] = pontos
                            else:
                                print("troxa")
                            
                            output = open("ranking.pkl",'wb')

                            pickle.dump(jog, output)
                            pickle.dump(pon, output)

                            output.close()
                            
                            frame_jogo_left.destroy()
                            frame_jogo_right.destroy()
                            titulo_frame.destroy()

                            frame_game_over = Frame(root, style='Title.TFrame')
                            frame_game_over.place(height=600, width=800, x=0, y=0)
                            frame_game_over.config()

                            image_game_over = PhotoImage(file="Imagens\\gameover.png")
                            label_game_over = Label(frame_game_over, image=image_game_over, style='GO.TLabel')
                            label_game_over.image = image_game_over
                            label_game_over.pack(padx=215, pady=20)

                            label_pontuacao = Label(frame_game_over, text=("Pontuação: " + str(pontos)),
                                                    style='GO.TLabel', font=("", 30))
                            label_pontuacao.pack()

                            def voltar2():
                                root.destroy()
                                newroot = Tk()
                                newroot.geometry("800x600+50+50")
                                App(newroot)
                                newroot.mainloop()

                            voltar2 = Button(frame_game_over, text="Voltar", style='MenuButtons.TButton',
                                            command=voltar2)
                            voltar2.pack(pady=20)

                        output = open("save.pkl", 'wb')
                        
                        pickle.dump(difi, output)
                        pickle.dump(nome2, output)
                        pickle.dump(pontos, output)
                        pickle.dump(dPontos, output)
                        pickle.dump(erros, output)
                        pickle.dump(palavra, output)
                        pickle.dump(palavra_auxiliar, output)
                        
                        
                        output.close()
                    else:
                        inputFile = open("save.pkl", 'rb')
                        
                        difi = pickle.load(inputFile)
                        nome2 = pickle.load(inputFile)
                        pontos = pickle.load(inputFile)
                        dPontos = pickle.load(inputFile)
                        erros = pickle.load(inputFile)
                        palavra_auxiliar = pickle.load(inputFile)
                        
                        inputFile.close()
                        palavra_auxiliar = list(palavra_auxiliar)

                        while palavra_auxiliar.count(letra) > 0:
                            index = palavra_auxiliar.index(letra)
                            palavra_auxiliar[index] = "-"

                            pontos = str(int(pontos)+100)

                            entry_letras[index].state(["!disabled"])
                            entry_letras[index].insert(0, letra)
                            entry_letras[index].state(["disabled"])
                            completo.append("-")
                            
                        output = open("save.pkl",'wb')

                        pickle.dump(difi, output)
                        pickle.dump(nome2, output)
                        pickle.dump(pontos, output)
                        pickle.dump(dPontos, output)
                        pickle.dump(erros, output)
                        pickle.dump(palavra, output)
                        pickle.dump(palavra_auxiliar, output)
                        pickle.dump(palavra_auxiliar, output)
                        

                        output.close()


                        if len(completo) == len(palavra_auxiliar):
                            inputFile = open("ranking.pkl", 'rb')
                            
                            jog = pickle.load(inputFile)
                            pon = pickle.load(inputFile)
                            
                            inputFile.close()

                            if (int(pontos) - pon[4]) > 0:
                                if (int(pontos) - pon[3]) > 0:
                                    if (int(pontos) - pon[2]) > 0:
                                        if (int(pontos) - pon[1]) > 0:
                                            if (int(pontos) - pon[0]) > 0:
                                                jog[4] = jog[3]
                                                pon[4] = pon[3]
                                                jog[3] = jog[2]
                                                pon[3] = pon[2]
                                                jog[2] = jog[1]
                                                pon[2] = pon[1]
                                                jog[1] = jog[0]
                                                pon[1] = pon[0]
                                                jog[0] = nome2
                                                pon[0] = pontos
                                            else:
                                                jog[5] = jog[4]
                                                pon[5] = pon[4]
                                                jog[4] = jog[3]
                                                pon[4] = pon[3]
                                                jog[3] = jog[2]
                                                pon[3] = pon[2]
                                                jog[2] = nome2
                                                pon[2] = pontos
                                        else:
                                            jog[4] = jog[3]
                                            pon[4] = pon[3]
                                            jog[3] = jog[2]
                                            pon[3] = pon[2]
                                            jog[2] = nome2
                                            pon[2] = pontos
                                    else:
                                        jog[4] = jog[3]
                                        pon[4] = pon[3]
                                        jog[3] = nome2
                                        pon[3] = pontos
                                else:
                                    jog[4] = nome2
                                    pon[4] = pontos
                            else:
                                print("troxa")
                            
                            output = open("ranking.pkl",'wb')

                            pickle.dump(jog, output)
                            pickle.dump(pon, output)

                            output.close()

                            
                            frame_jogo_left.destroy()
                            frame_jogo_right.destroy()
                            titulo_frame.destroy()

                            frame_congra = Frame(root, style='Plac.TFrame')
                            frame_congra.place(height=600, width=800, x=0, y=0)
                            frame_congra.config()

                            image_cong = PhotoImage(file="Imagens\\congratulations.png")

                            lp = Label(frame_congra, image=image_cong)
                            lp.image = image_cong
                            lp.pack(side="top")
                            lp = Label(frame_congra, text=("Pontuação: " + pontos), font=("", 30))
                            lp.pack(pady=50)

                            def voltar():
                                root.destroy()
                                newroot = Tk()
                                newroot.geometry("800x600+50+50")
                                App(newroot)
                                newroot.mainloop()

                            voltar = Button(frame_congra, text="Voltar", style='MenuButtons.TButton',
                                            command=voltar)
                            voltar.pack()

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
                        array_buttons.append(Button(frame1, text=array_letras[i], style='words.TButton',
                                                    command=lambda name=i: jogar_letra(array_letras[name])))
                        array_buttons[i].pack(pady=10)
                    elif x == 2:
                        array_buttons.append(Button(frame2, text=array_letras[i], style='words.TButton',
                                                    command=lambda name=i: jogar_letra(array_letras[name])))
                        array_buttons[i].pack(pady=10)
                    elif x == 3:
                        array_buttons.append(Button(frame3, text=array_letras[i], style='words.TButton',
                                                    command=lambda name=i: jogar_letra(array_letras[name])))
                        array_buttons[i].pack(pady=10)
                    elif x == 4:
                        array_buttons.append(Button(frame4, text=array_letras[i], style='words.TButton',
                                                    command=lambda name=i: jogar_letra(array_letras[name])))
                        array_buttons[i].pack(pady=10)
                        x = 0
                    x += 1

            iniciar = Button(frame_iniciar_jogo, text="Iniciar", style='MenuButtons.TButton', command=iniciar)

            def callback(nome):
                if nome.get() != "":
                    iniciar.state(["!disabled"])
                else:
                    iniciar.state(["disabled"])

            
            def voltar():
                root.destroy()
                newroot = Tk()
                newroot.geometry("800x600+50+50")
                App(newroot)
                newroot.mainloop()

            iniciar.pack(pady=50)
            iniciar.state(["disabled"])

            voltar = Button(frame_iniciar_jogo, text="Voltar", style='MenuButtons.TButton', command=voltar)
            voltar.pack()

        def placar():
            inputFile = open("ranking.pkl", 'rb')
                            
            jog = pickle.load(inputFile)
            pon = pickle.load(inputFile)
                            
            inputFile.close()


            
            
            main_frame.destroy()
            frame_placar = Frame(root, style='Plac.TFrame')
            frame_placar.place(height=600, width=800, y=0)
            frame_placar.config()

            titulo_frame = Frame(root, style='Title.TFrame')
            titulo_frame.place(height=100, width=800)
            titulo_frame.config()

            titulo = Label(titulo_frame, text="JOGO DA FORCA", style='T.TLabel')
            titulo.pack(pady=20)

            frame_colocacao1 = Frame(frame_placar, style='Plac.TFrame')
            frame_colocacao1.place(height=160, width=120, x=340, y=160)
            frame_colocacao1.config()
            frame_colocacao2 = Frame(frame_placar, style='Plac.TFrame')
            frame_colocacao2.place(height=160, width=120, x=170, y=220)
            frame_colocacao2.config()
            frame_colocacao3 = Frame(frame_placar, style='Plac.TFrame')
            frame_colocacao3.place(height=160, width=120, x=510, y=220)
            frame_colocacao3.config()
            frame_colocacao4 = Frame(frame_placar, style='Plac.TFrame')
            frame_colocacao4.place(height=160, width=120, x=170, y=400)
            frame_colocacao4.config()
            frame_colocacao5 = Frame(frame_placar, style='Plac.TFrame')
            frame_colocacao5.place(height=160, width=120, x=510, y=400)
            frame_colocacao5.config()

            image_primeiro = PhotoImage(file="Imagens\\primeiro.png")
            image_outros = PhotoImage(file="Imagens\\outros.png")

            lp = Label(frame_colocacao1, image=image_primeiro)
            lp.image = image_primeiro
            lp.pack(side="top")
            lp = Label(frame_colocacao2, image=image_outros)
            lp.image = image_outros
            lp.pack(side="top")
            lp = Label(frame_colocacao3, image=image_outros)
            lp.image = image_outros
            lp.pack(side="top")
            lp = Label(frame_colocacao4, image=image_outros)
            lp.image = image_outros
            lp.pack(side="top")
            lp = Label(frame_colocacao5, image=image_outros)
            lp.image = image_outros
            lp.pack(side="top")

            lp = Label(frame_colocacao1, text=jog[0], style="Dp.TLabel", font=("", 10))
            lp.pack(side="bottom")
            lp = Label(frame_colocacao1, text=pon[0], style="Dp.TLabel", font=("", 10))
            lp.pack(side="bottom")
            lp = Label(frame_colocacao2, text=jog[1], style="Dp.TLabel", font=("", 10))
            lp.pack(side="bottom")
            lp = Label(frame_colocacao2, text=pon[1], style="Dp.TLabel", font=("", 10))
            lp.pack(side="bottom")
            lp = Label(frame_colocacao3, text=jog[2], style="Dp.TLabel", font=("", 10))
            lp.pack(side="bottom")
            lp = Label(frame_colocacao3, text=pon[2], style="Dp.TLabel", font=("", 10))
            lp.pack(side="bottom")
            lp = Label(frame_colocacao4, text=jog[3], style="Dp.TLabel", font=("", 10))
            lp.pack(side="bottom")
            lp = Label(frame_colocacao4, text=pon[3], style="Dp.TLabel", font=("", 10))
            lp.pack(side="bottom")
            lp = Label(frame_colocacao5, text=jog[4], style="Dp.TLabel", font=("", 10))
            lp.pack(side="bottom")
            lp = Label(frame_colocacao5, text=pon[4], style="Dp.TLabel", font=("", 10))
            lp.pack(side="bottom")

        novo_jogo = Button(main_frame, text="        Novo Jogo       ", style='MenuButtons.TButton', command=novojogo)
        novo_jogo.pack(pady=20)
        continuar_jogo = Button(main_frame, text="     Continuar Jogo    ", style='MenuButtons.TButton', command=contjogo)
        continuar_jogo.pack(pady=20)
##        continuar_jogo.state(['disabled'])
        placares_jogo = Button(main_frame, text="         Placares         ", style='MenuButtons.TButton', command=placar)
        placares_jogo.pack(pady=20)
        gerenciar_palavras = Button(main_frame, text="  Gerenciar Palavras ", style='MenuButtons.TButton')
        gerenciar_palavras.pack(pady=20)
        gerenciar_palavras.state(['disabled'])

root = Tk()
root.geometry("800x600+50+50")
App(root)
root.mainloop()
