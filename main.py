# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
window = Tk()       # Create the application window

window.geometry('350x200') # set window size

# Add a label with the text "Hello"
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

big = Label(window, text="Hello", font=("Arial Bold", 50))
big.grid(column=0,row=3)

l1 = Label(window, text="h")
l1.grid(column=0, row=1)


txt = Entry(window,width=10)
txt.grid(column=1, row=0)

