def novojogo():
            main_frame.destroy()
            frame_iniciar_jogo = Frame(root, style='Container.TFrame')
            frame_iniciar_jogo.place(height=400, width=800, y=160)
            frame_iniciar_jogo.config()

            lbl_nome_jogador = Label(frame_iniciar_jogo, text="Nome do Jogador: ", style='D.TLabel')
            lbl_nome_jogador.pack(pady=20)

            def iniciar():
                difi = lista.get()
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

                palavra_auxiliar = list(palavra)
                print(palavra)
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

                palavra = palavra.upper()

                def jogar_letra(letra):
                    index = array_letras.index(letra)
                    array_buttons[index].state(["disabled"])

                    palavra_auxiliar = list(palavra)
                    if palavra.count(letra) == 0:
                        inputFile = open("save.pkl", 'rb')
                        difi = pickle.load(inputFile)
                        nome2 = pickle.load(inputFile)
                        pontos = pickle.load(inputFile)
                        dPontos = pickle.load(inputFile)
                        erros = pickle.load(inputFile)
                        inputFile.close()
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
                        
                        output.close()
                    else:
                        inputFile = open("save.pkl", 'rb')
                        difi = pickle.load(inputFile)
                        nome2 = pickle.load(inputFile)
                        pontos = pickle.load(inputFile)
                        dPontos = pickle.load(inputFile)
                        erros = pickle.load(inputFile)
                        inputFile.close()

                        while palavra_auxiliar.count(letra) > 0:
                            index = palavra_auxiliar.index(letra)
                            palavra_auxiliar[index] = "-"

                            pontos = str(int(pontos)+100)

                            entry_letras[index].state(["!disabled"])
                            entry_letras[index].insert(0, letra)
                            entry_letras[index].state(["disabled"])
                            completo.append("-")
                        output = open("save.pkl", 'wb')
                        pickle.dump(difi, output)
                        pickle.dump(nome2, output)
                        pickle.dump(pontos, output)
                        pickle.dump(dPontos, output)
                        pickle.dump(erros, output)
                        output.close()


                        if len(completo) == len(palavra_auxiliar):
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















                difi = pickle.load(inputFile)
                nome2 = pickle.load(inputFile)
                pontos = pickle.load(inputFile)
                dPontos = pickle.load(inputFile)
                erros = pickle.load(inputFile)
                palavra = pickle.load(inputFile)
                palavra_auxiliar = pickle.load(inputFile)
                ativadas = pickle.load(inputFile)

                ativadas = list(ativadas)
                palavra_auxiliar = list(palavra_auxiliar)





                pickle.dump(difi, output)
                pickle.dump(nome2, output)
                pickle.dump(pontos, output)
                pickle.dump(dPontos, output)
                pickle.dump(erros, output)
                pickle.dump(palavra, output)
                pickle.dump(palavra_auxiliar, output)
                pickle.dump(ativadas, output)
