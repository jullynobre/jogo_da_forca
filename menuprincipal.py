from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("800x600+50+50")

s = Style()
s.configure('Title.TFrame', background='#00008D')
s.configure('Container.TFrame', background='#C8C4FF')

titulo_frame = Frame(root, style='Title.TFrame')
titulo_frame.place(height=100, width=800)
titulo_frame.config()

left_frame = Frame(root, style='Container.TFrame')
left_frame.place(height=400, width=325, x=50, y=150)
left_frame.config()

right_frame = Frame(root, style='Container.TFrame')
right_frame.place(height=400, width=325, x=425, y=150)
right_frame.config()

root.mainloop()
