# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

    

import tkinter as tk
import os

mainWindow = tk.Tk()
mainWindow.title('Calculator')
mainWindow.geometry('640x480-8-200')


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def button_operation(operator):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + operator)
    
    
# Configure the grid column to expand with the window
for i in range(7):
    mainWindow.grid_columnconfigure(i, weight=1)
for i in range(10):
    mainWindow.grid_rowconfigure(i, weight=1)
    
    
# Create an Entry widget and place it in the grid
entry = tk.Entry(mainWindow)
entry.grid(row=0, column=0, columnspan=4, sticky='ew')

button1 = tk.Button(mainWindow, text='1', width=2, height=2, command=lambda: button_click(1))
button1.grid(row=1, column=0, sticky='nsew')
button2 = tk.Button(mainWindow, text='2', width=2, height=2, command=lambda: button_click(2))
button2.grid(row=1, column=1, sticky='nsew')
button3 = tk.Button(mainWindow, text='3', width=2, height=2, command=lambda: button_click(3))
button3.grid(row=1, column=2, sticky='nsew')
button4 = tk.Button(mainWindow, text='4', width=2, height=2, command=lambda: button_click(4))
button4.grid(row=2, column=0, sticky='nsew')
button5 = tk.Button(mainWindow, text='5', width=2, height=2, command=lambda: button_click(5))
button5.grid(row=2, column=1, sticky='nsew')
button6 = tk.Button(mainWindow, text='6', width=2, height=2, command=lambda: button_click(6))
button6.grid(row=2, column=2, sticky='nsew')
button7 = tk.Button(mainWindow, text='7', width=2, height=2, command=lambda: button_click(7))
button7.grid(row=3, column=0, sticky='nsew')
button8 = tk.Button(mainWindow, text='8', width=2, height=2, command=lambda: button_click(8))
button8.grid(row=3, column=1, sticky='nsew')
button9 = tk.Button(mainWindow, text='9', width=2, height=2, command=lambda: button_click(9))
button9.grid(row=3, column=2, sticky='nsew')
thebutton= tk.Button(mainWindow, text='0', width=2, height=2,command=lambda: button_click(9))
thebutton.grid(row=4, column=0, sticky='nsew')


#operators
button1 = tk.Button(mainWindow, text='1', width=2, height=2)
button1.grid(row=1, column=0, sticky='nsew')
button2 = tk.Button(mainWindow, text='2', width=2, height=2)
button2.grid(row=1, column=1, sticky='nsew')
button3 = tk.Button(mainWindow, text='3', width=2, height=2)
button3.grid(row=1, column=2, sticky='nsew')
button4 = tk.Button(mainWindow, text='4', width=2, height=2)
button4.grid(row=2, column=0, sticky='nsew')
button1 = tk.Button(mainWindow, text='1', width=2, height=2)
button1.grid(row=1, column=0, sticky='nsew')


# Create operation buttons
button_add = tk.Button(mainWindow, text='+', width=2, height=2, command=lambda: button_operation('+'))
button_add.grid(row=1, column=3, sticky='nsew')
button_subtract = tk.Button(mainWindow, text='-', width=2, height=2, command=lambda: button_operation('-'))
button_subtract.grid(row=2, column=3, sticky='nsew')
button_multiply = tk.Button(mainWindow, text='*', width=2, height=2, command=lambda: button_operation('*'))
button_multiply.grid(row=3, column=3, sticky='nsew')
button_divide = tk.Button(mainWindow, text='/', width=2, height=2, command=lambda: button_operation('/'))
button_divide.grid(row=4, column=3, sticky='nsew')

# Create equal and clear buttons
button_equal = tk.Button(mainWindow, text='=', width=2, height=2, command=button_equal)
button_equal.grid(row=4, column=2, sticky='nsew')
button_clear = tk.Button(mainWindow, text='C', width=2, height=2, command=button_clear)
button_clear.grid(row=4, column=1, sticky='nsew')


mainWindow.mainloop()




