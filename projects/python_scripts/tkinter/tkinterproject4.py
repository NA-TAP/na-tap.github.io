from tkinter import *
clicks = 0
def click():
    global clicks
    clicks += 1
    label.config(text=clicks)
    #label2.pack()



window =  Tk()
imgpath = 'horse.png'
image = PhotoImage(file=imgpath)
button = Button(window,text="Click Me!!!")
button.config(command=click) # Don't put "()" in click()
button.config(font=('Nata Sans',50,'bold'))
button.config(bg="#ff5500")
button.config(fg="#ffff00")
button.config(activebackground="#88ff00")
button.config(activeforeground="#0015ff")
button.config(image=image)
button.config(compound='bottom') # Can also use 'top','left','right',or 'none'
#button.config(state=DISABLED) #disables button (ACTIVE/DISABLED)
label = Label(window,text=clicks,font=('Nata Sans',50,'bold'))
label.pack()
button.pack()
label2=Label(window,image=image)
window.mainloop()