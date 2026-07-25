from tkinter import *

window = Tk() # istantiate an instance of a window
window.geometry('420x300')
window.title('Bro Code first Gui program')
icon = PhotoImage(file='horse.png')
window.iconphoto(True, icon)
window.config(background="#64e6e9")
window.mainloop() #place window on computer screen, listen for events
