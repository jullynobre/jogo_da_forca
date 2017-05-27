from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("800x600+50+50")

s = Style()

s.configure('Title.TFrame', background='#00008D')
s.configure('Container.TFrame')
s.configure('T.TLabel', background="#00008D", foreground="white", font=("", 35))
s.configure('MenuButtons.TButton', highlightbackground="#C8C4FF", foreground="#00008D", font=("", 15))

titulo_frame = Frame(root, style='Title.TFrame')
titulo_frame.place(height=100, width=800)
titulo_frame.config()

titulo = Label(titulo_frame, text="JOGO DA FORCA", style='T.TLabel')
titulo.pack(pady=20)

main_frame = Frame(root, style='Container.TFrame')
main_frame.place(height=400, width=800, y=160)
main_frame.config()

novo_jogo = Button(main_frame, text="        Novo Jogo       ", style='MenuButtons.TButton')
novo_jogo.pack(pady=20)
continuar_jogo = Button(main_frame, text="     Continuar Jogo    ", style='MenuButtons.TButton')
continuar_jogo.pack(pady=20)
placares_jogo = Button(main_frame, text="         Placares         ", style='MenuButtons.TButton')
placares_jogo.pack(pady=20)
gerenciar_palavras = Button(main_frame, text="  Gerenciar Palavras ", style='MenuButtons.TButton')
gerenciar_palavras.pack(pady=20)

root.mainloop()
