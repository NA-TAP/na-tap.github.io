from tkinter import *

def display():
    if (x.get()==1)&(y.get()==1):
        print('I like python and java')
    elif (x.get()==1)&(y.get()!=1):
        print('I like python but not java')
    elif (x.get()!=1)&(y.get()==1):
        print('I like java but not python')
    else:
        print('I don\'t like python or java')






window = Tk()
pylogo = PhotoImage(file='python.png')
javalogo = PhotoImage(file='java.png')


x = IntVar()
y = IntVar()
checkbox = Checkbutton(window,text='Python',variable=x,onvalue=1,offvalue=0,command=display)
checkbox.config(font=('Mojangles', 15))
checkbox.config(fg = '#4eaa34')
checkbox.config(bg = 'brown')
checkbox.config(activebackground='brown')
checkbox.config(activeforeground='#43aa34')
checkbox.config(image=pylogo,compound='right')
checkbox.config(padx=10,width=350)
checkbox.config(pady=10,height=300)
checkbox.config(anchor='w')
checkbox.pack()

checkbox2 = Checkbutton(window,text='Java',variable=y,onvalue=1,offvalue=0,command=display)
checkbox2.config(font=('Mojangles', 15))
checkbox2.config(fg = '#4eaa34')
checkbox2.config(bg = 'brown')
checkbox2.config(activebackground='brown')
checkbox2.config(activeforeground='#43aa34')
checkbox2.config(image=javalogo,compound='right')
checkbox2.config(padx=10,width=350)
checkbox2.config(pady=10,height=300)
checkbox2.config(anchor='w')
checkbox2.pack()
window.mainloop()