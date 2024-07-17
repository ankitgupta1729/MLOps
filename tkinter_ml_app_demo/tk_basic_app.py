from tkinter import *
win = Tk()
a = Label(win, text ="Hello World")
a.pack()
b=Button(win, text='Exit', command=win.destroy)
b.pack()
win.mainloop()
