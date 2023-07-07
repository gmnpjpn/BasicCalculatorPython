from tkinter import *

window = Tk()
window.title("Python Calculator with Tkinter")

i = 0 # Global index for the positions at entry

# Entry
e_text = Entry(window, font = ("Calibri 20"))
e_text.grid(row = 0, column = 0, columnspan = 4, padx = 50, pady = 5)

# Functions
def click_btn(valor):
    global i
    e_text.insert(i, valor)
    i += 1

def click_delete():
    e_text.delete(0, END)

def operation():
    ecuation = e_text.get()
    result = eval(ecuation)
    e_text.delete(0, END)
    e_text.insert(0, result)
    i = 0

# Buttons
button1 = Button(window, text = "1", width = 5, height = 2, command = lambda: click_btn(1))
button2 = Button(window, text = "2", width = 5, height = 2, command = lambda: click_btn(2))
button3 = Button(window, text = "3", width = 5, height = 2, command = lambda: click_btn(3))
button4 = Button(window, text = "4", width = 5, height = 2, command = lambda: click_btn(4))
button5 = Button(window, text = "5", width = 5, height = 2, command = lambda: click_btn(5))
button6 = Button(window, text = "6", width = 5, height = 2, command = lambda: click_btn(6))
button7 = Button(window, text = "7", width = 5, height = 2, command = lambda: click_btn(7))
button8 = Button(window, text = "8", width = 5, height = 2, command = lambda: click_btn(8))
button9 = Button(window, text = "9", width = 5, height = 2, command = lambda: click_btn(9))
button0 = Button(window, text = "0", width = 13, height = 2, command = lambda: click_btn(0))

button_delete = Button(window, text = "AC", width = 5, height = 2, command = lambda: click_delete())
button_ParenthesisOpen = Button(window, text = "(", width = 5, height = 2, command = lambda: click_btn("("))
button_ParenthesisClose = Button(window, text = ")", width = 5, height = 2, command = lambda: click_btn(")"))
button_dot = Button(window, text = ".", width = 5, height = 2, command = lambda: click_btn("."))

button_div = Button(window, text = "/", width = 5, height = 2, command = lambda: click_btn("/"))
button_mult = Button(window, text = "*", width = 5, height = 2, command = lambda: click_btn("*"))
button_sum = Button(window, text = "+", width = 5, height = 2, command = lambda: click_btn("+"))
button_sub = Button(window, text = "-", width = 5, height = 2, command = lambda: click_btn("-"))
button_equals = Button(window, text = "=", width = 5, height = 2, command = lambda: operation())

# Show buttons
button_delete.grid(row = 1, column = 0, padx = 5, pady = 5)
button_ParenthesisOpen.grid(row = 1, column = 1, padx = 5, pady = 5)
button_ParenthesisClose.grid(row = 1, column = 2, padx = 5, pady = 5)
button_div.grid(row = 1, column = 3, padx = 5, pady = 5)

button7.grid(row = 2, column = 0, padx = 5, pady = 5)
button8.grid(row = 2, column = 1, padx = 5, pady = 5)
button9.grid(row = 2, column = 2, padx = 5, pady = 5)
button_mult.grid(row = 2, column = 3, padx = 5, pady = 5)

button4.grid(row = 3, column = 0, padx = 5, pady = 5)
button5.grid(row = 3, column = 1, padx = 5, pady = 5)
button6.grid(row = 3, column = 2, padx = 5, pady = 5)
button_sum.grid(row = 3, column = 3, padx = 5, pady = 5)

button2.grid(row = 4, column = 1, padx = 5, pady = 5)
button3.grid(row = 4, column = 2, padx = 5, pady = 5)
button1.grid(row = 4, column = 0, padx = 5, pady = 5)
button_sub.grid(row = 4, column = 3, padx = 5, pady = 5)

button0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
button_dot.grid(row = 5, column = 2, padx = 5, pady = 5)
button_equals.grid(row = 5, column = 3, padx = 5, pady = 5)

window.mainloop()