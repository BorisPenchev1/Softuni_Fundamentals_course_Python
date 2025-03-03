from tkinter import *

window = Tk()

window.title("click counter")

count = 0

def clicked():
    global count
    count += 1
    lbl.config(text=count)

lbl = Label(window, text=count)
lbl.pack()
lbl.config(font=('Monospace', 50))

btn = Button(window, text="Click Me")
btn.config(command=clicked)
btn.config(font=('Ink Free', 50, 'bold'), bg = '#ff6200', fg='fffb1f', activebackground='FF0000', activeforeground='fffb1f')
btn.grid(column=0, row=1)
btn.pack()


window.mainloop()
