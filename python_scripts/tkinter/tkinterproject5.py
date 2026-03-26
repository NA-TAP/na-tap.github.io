from tkinter import *

def submit():
    username = entry.get()
    print('Hello',username)
def delete():
    entry.delete(0,END) # Deletes one line
def bspace():
    entry.delete(len(entry.get())-1, END)


window = Tk()
sumbitbutton = Button(window,text="Submit",font=('Mojangles', 10),command=submit)
sumbitbutton.pack(side=RIGHT)
deletebutton = Button(window,text="Delete",font=('Mojangles', 10),command=delete)
deletebutton.pack(side=RIGHT)
bspacebutton = Button(window,text="Backspace",font=('Mojangles', 10),command=bspace)
bspacebutton.pack(side=RIGHT)
entry = Entry()
entry.config(font=('Mojangles', 40))
entry.config(bg='#111111')
entry.config(fg='#efefef')
#entry.insert(0,"Hello there")
#entry.config(state=DISABLED)
entry.config(width=10)
#entry.config(show='$')
entry.pack()
window.mainloop()

