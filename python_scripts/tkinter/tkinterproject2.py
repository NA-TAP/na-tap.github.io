from tkinter import *

window = Tk()

photo= PhotoImage(file='horse.png')

label = Label(window,text='Hello World',
              font=('Arial', 40, 'bold'),
              fg='#2D94D3',
              bg='#111111',
              relief=RAISED, # other styles are SUNKEN,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom') # We can also put lop, left, and right
label.pack()
# label.place(x=0,y=0)


window.mainloop()