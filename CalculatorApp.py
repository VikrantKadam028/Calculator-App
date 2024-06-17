
from tkinter import *

root = Tk()
root.title("CALCULATOR APP")
root.geometry("300x420")

expression = ''

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equals():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression = ""
    except:
        equation.set("error")
        expression = ""    

def clear_expression():
    global expression
    expression = ""
    equation.set("")

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

frame = Frame(root, pady=10, relief=RAISED, bd=5)
frame.pack()
framenum5 = Frame(root, bd=5)
framenum5.pack()
framenum1 = Frame(root, bd=5)
framenum1.pack()
framenum2 = Frame(root, bd=5)
framenum2.pack()
framenum3 = Frame(root, bd=5)
framenum3.pack()
framenum4 = Frame(root, bd=5)
framenum4.pack()

equation = StringVar()
entry = Entry(frame, font=('Helvetica', 20), width=30, textvariable=equation)
entry.pack()

# framenum5
clear_button = Button(framenum5, text="Clear", width=10, padx=5, pady=5, font=('Helvetica', 14, 'bold'), bd=5, command=clear_expression,bg="black",fg="white")
clear_button.pack(side=LEFT)
back = Button(framenum5, text="Del", width=10, padx=5, pady=5, font=('Helvetica', 14, 'bold'), bd=5, command=backspace,bg="black",fg="white")
back.pack(side=LEFT)

# framenum1
button1 = Button(framenum1, text="7", width=3, padx=10, pady=10, font=('Helvetica', 16, 'bold'), bd=5, command=lambda: press(7))
button1.pack(side=LEFT)
button2 = Button(framenum1, text="8", width=3, padx=10, pady=10, font=('Helvetica', 16, 'bold'), bd=5, command=lambda: press(8))
button2.pack(side=LEFT)
button3 = Button(framenum1, text="9", width=3, padx=10, pady=10, font=('Helvetica', 16, 'bold'), bd=5, command=lambda: press(9))
button3.pack(side=LEFT)
plus = Button(framenum1, text="+", width=3, padx=10, pady=10, font=('Helvetica', 16, 'bold'), bd=5, command=lambda: press("+"))
plus.pack(side=LEFT)

# framenum2
button4 = Button(framenum2, text="4", width=3, padx=10, pady=10, font=('Helvetica', 16, 'bold'), bd=5, command=lambda: press(4))
button4.pack(side=LEFT)
button5 = Button(framenum2, text="5", width=3, padx=10, pady=10, font=('Helvetica', 16, 'bold'), bd=5, command=lambda: press(5))
button5.pack(side=LEFT)
button6 = Button(framenum2, text="6", width=3, padx=10, pady=10, font=('Helvetica', 16, 'bold'), bd=5, command=lambda: press(6))
button6.pack(side=LEFT)
minus = Button(framenum2, text="-", width=3, padx=10, pady=10, font=('Helvetica', 16, 'bold'), bd=5, command=lambda: press("-"))
minus.pack(side=LEFT)

# framenum3
button7 = Button(framenum3, text="1", width=3, padx=10, pady=10, font=('Helvetica', 16, 'bold'), bd=5, command=lambda: press(1))
button7.pack(side=LEFT)
button8 = Button(framenum3, text="2", width=3, padx=10, pady=10, font=('Helvetica', 16, 'bold'), bd=5, command=lambda: press(2))
button8.pack(side=LEFT)
button9 = Button(framenum3, text="3", width=3, padx=10, pady=10, font=('Helvetica', 16, 'bold'), bd=5, command=lambda: press(3))
button9.pack(side=LEFT)
mul = Button(framenum3, text="*", width=3, padx=10, pady=10, font=('Helvetica', 16, 'bold'), bd=5, command=lambda: press("*"))
mul.pack(side=LEFT)

# framenum4
button0 = Button(framenum4, text="0", width=3, padx=10, pady=10, font=('Helvetica', 16, 'bold'), bd=5, command=lambda: press(0))
button0.pack(side=LEFT)
equal = Button(framenum4, text="=", width=8, padx=10, pady=10, font=('Helvetica', 16, 'bold'), bg="orange", bd=5, command=equals)
equal.pack(side=LEFT)

div = Button(framenum4, text="/", width=3, padx=10, pady=10, font=('Helvetica', 16, 'bold'), bd=5, command=lambda: press("/"))
div.pack(side=LEFT)

root.mainloop()
