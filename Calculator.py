import tkinter as tk
from tkinter import *
root = tk.Tk()
icon = tk.PhotoImage(file='calculator.png')
root.tk.call('wm','iconphoto', root._w, icon)
root.title("calculator")
root.pack_propagate(False)
root.resizable(0,0)

e = tk.Entry(root, width=35, border=5)
e.config(bg = 'black', fg = 'white')
e.grid(row=0, column= 0, columnspan=4)


def number(math):
    #e.delete(0, tk.END)
    global first
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0,str(current) + str(math))

def clear():
    e.delete(0, tk.END)

def addition():
    global first
    global const
    const = "addition"
    first = float(e.get())
    e.delete(0, tk.END)
    
def multiplication():
    global first
    global const
    const = "multiplication"
    first = float(e.get())
    e.delete(0, tk.END)

def division():
    global first
    global const
    const = "division"
    first = float(e.get())
    e.delete(0, tk.END)
def subtraction():
    global first
    global const
    const = "subtracttion"
    first = float(e.get())
    e.delete(0, tk.END)

def equal():
    second = float(e.get())
    e.delete(0, tk.END)
    if const == "multiplication":
        c = first * second
        e.insert(0, str(c))
    elif const == "addition":
        c = first + second
        e.insert(0, str(c))
    elif const == "subtracttion":
        c = first - second
        e.insert(0, str(c))
    elif const == "division":
        c = first / second
        e.insert(0, str(c))
    else:
        pass
    

btn1 = tk.Button(root, text = "1",font = ("arial", 18), bg = 'grey', command = lambda: number(1))
btn2 = tk.Button(root, text = "2",font = ("arial", 18), bg = 'grey', command = lambda: number(2))
btn3 = tk.Button(root, text = "3",font = ("arial", 18), bg = 'grey', command = lambda: number(3))
btn4 = tk.Button(root, text = "4",font = ("arial", 18), bg = 'grey', command = lambda: number(4))
btn5 = tk.Button(root, text = "5",font = ("arial", 18), bg = 'grey', command = lambda: number(5))
btn6 = tk.Button(root, text = "6",font = ("arial", 18), bg = 'grey', command = lambda: number(6))
btn7 = tk.Button(root, text = "7",font = ("arial", 18), bg = 'grey', command = lambda: number(7))
btn8 = tk.Button(root, text = "8",font = ("arial", 18), bg = 'grey', command = lambda: number(8))
btn9 = tk.Button(root, text = "9",font = ("arial", 18), bg = 'grey', command = lambda: number(9))
btn10 = tk.Button(root, text = "0",font = ("arial", 18), bg = 'grey', command = lambda: number(0))
btn11 = tk.Button(root, text = "/",font = ("arial", 18), bg = 'thistle4', command = division)
btn12 = tk.Button(root, text = "+",font = ("arial", 18), bg = 'thistle4', command = addition)
btn13 = tk.Button(root, text = "-",font = ("arial", 18), bg = 'thistle4', command = subtraction)
btn14 = tk.Button(root, text = "x",font = ("arial", 18), bg = 'thistle4', command = multiplication)
btn15 = tk.Button(root, text = "AC",font = ("arial", 18), bg = 'grey70', command = clear)
btn16 = tk.Button(root, text = "=",font = ("arial", 18), bg = 'thistle4', command = equal)
btn17 = tk.Button(root, text = ".",font = ("arial", 18), bg = 'grey', command = lambda: number('.'))




btn1.grid(row = 4, column = 0, sticky = tk.W + tk.E)
btn2.grid(row = 4, column = 1, sticky = tk.W + tk.E)
btn3.grid(row = 4, column = 2, sticky = tk.W + tk.E)
btn4.grid(row = 3, column = 0, sticky = tk.W + tk.E)
btn5.grid(row = 3, column = 1, sticky = tk.W + tk.E)
btn6.grid(row = 3, column = 2, sticky = tk.W + tk.E)
btn7.grid(row = 2, column = 0, sticky = tk.W + tk.E)
btn8.grid(row = 2, column = 1, sticky = tk.W + tk.E)
btn9.grid(row = 2, column = 2, sticky = tk.W + tk.E)
btn10.grid(row = 5, column = 0, columnspan=2, sticky = tk.W + tk.E)
btn11.grid(row = 1, column = 1, sticky = tk.W + tk.E)
btn12.grid(row = 2, column = 3, rowspan=2, sticky = tk.W + tk.E + tk.N + tk.S)
btn13.grid(row = 1, column = 3, sticky = tk.W + tk.E)
btn14.grid(row = 1, column = 2, sticky = tk.W + tk.E + tk.N + tk.S)
btn15.grid(row = 1, column = 0,sticky = tk.W + tk.E)
btn16.grid(row = 4, column = 3, rowspan=2, sticky = tk.W + tk.E + tk.N + tk.S)
btn17.grid(row = 5, column = 2, sticky = tk.W + tk.E)

root.mainloop()
