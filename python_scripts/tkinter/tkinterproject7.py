from tkinter import *

food = ['pizza','hamburger','hotdog']
def order():
    if (x.get()==0):
        print('you order pizza')
    elif (x.get()==1):
        print('you order hamburger')
    else:
        print('you order hotdoge')

window = Tk()
x= IntVar()
pizzimg = PhotoImage(file='horse.png')
hotimg = PhotoImage(file='java.png')
burgring = PhotoImage(file='python.png')
foodimgs=[pizzimg,burgring,hotimg]

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],
                              variable=x, # Groups radiobuttons
                              value=index, # gives different values so no all on/off at the same time
                              padx=25,
                              font=('5yearsoldfont',30),
                              image=foodimgs[index],
                              anchor='w',
                              compound='right',
                              width=415,
                              command=order)
    radiobutton.pack(anchor = 'w')

window.mainloop()