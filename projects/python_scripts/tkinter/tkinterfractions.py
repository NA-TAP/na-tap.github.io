from tkinter import *
import tkinter.messagebox as messagebox

def createfrac(n,d):
    # ₁¹₂²₃³₄⁴₅⁵₆⁶₇⁷₈⁸₉⁹₀⁰ ⁄

    nchars = ''
    dchars = ''
    suplist = ['⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹']
    for char in range(len(n)):
        nchars += suplist[int(n[char])]
    sublist = ['₀','₁','₂','₃','₄','₅','₆','₇','₈','₉']
    for char in range(len(d)):
        dchars += sublist[int(d[char])]
    returny = nchars + '⁄' + dchars
    return returny




window = Tk()
fraction = StringVar()

numerator = Entry()
numerator.config(font=('Times New Roman', 20))
numerator.config(bg='#111111')
numerator.config(fg='#efefef')
#numerator.insert(0,"Hello there")
#numerator.config(state=DISABLED)
numerator.config(width=10)
#numerator.config(show='$')
numerator.pack()

denominator = Entry()
denominator.config(font=('Times New Roman', 20))
denominator.config(bg='#111111')
denominator.config(fg='#efefef')
#denominator.insert(0,"Hello there")
#denominator.config(state=DISABLED)
denominator.config(width=10)
#denominator.config(show='$')
denominator.pack()

frac = Label(window, text='placeholder for fraction text',
              font=('Times New Roman', 20, 'bold'),
              fg='#2D94D3',
              bg='#111111',
              )
frac.pack()

def display_fraction():
    num = numerator.get()
    den = denominator.get()
    result = createfrac(num, den)
    frac.config(text=result)

def copy_to_clipboard():
    fraction_text = frac.cget('text')
    if fraction_text != 'placeholder for fraction text':
        window.clipboard_clear()
        window.clipboard_append(fraction_text)
        messagebox.showinfo('Copied', 'Fraction copied to clipboard!')
    else:
        messagebox.showwarning('Error', 'Please display a fraction first')

button = Button(window, text='Display Fraction', command=display_fraction,
                font=('Arial', 20), bg='#2D94D3', fg='#111111')
button.pack()

copy_button = Button(window, text='Copy to Clipboard', command=copy_to_clipboard,
                     font=('Arial', 20), bg='#2D94D3', fg='#111111')
copy_button.pack()

window.mainloop()
