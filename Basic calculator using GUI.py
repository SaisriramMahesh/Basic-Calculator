import tkinter
from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("580x590")
root.resizable(False, False)
root.configure(bg = "papaya whip")

equation = ""

def show(value):
	global equation
	equation += value
	label.config(text = equation)

def clear():
	global equation
	equation = ""
	label.config(text = equation)

def calculate():
	global equation
	result = ""
	if equation != "":
		try:
			result = eval(equation)
		except:
			result = "syntax error"
			equation = ""
	label.config(text = result)


label = Label(root, width = 25, height = 2, text = "", font = ("Lucida Console", 30), bd = 1, fg ="black", bg = "gray")
label.pack()

Button(root, text = "C", width = 5, height = 1, font = ("Lucida Console", 30, "bold"), bd = 1, fg ="black", bg = "light coral", command = lambda: clear()).place(x = 10, y = 100)
Button(root, text = "/", width = 5, height = 1, font = ("Lucida Console", 30, "bold"), bd = 1, fg ="black", bg = "gray", command = lambda: show("/")).place(x = 150, y = 100)
Button(root, text = "%", width = 5, height = 1, font = ("Lucida Console", 30, "bold"), bd = 1, fg ="black", bg = "gray", command = lambda: show("%")).place(x = 290, y = 100)
Button(root, text = "*", width = 5, height = 1, font = ("Lucida Console", 30, "bold"), bd = 1, fg ="black", bg = "gray", command = lambda: show("*")).place(x = 430, y = 100)


Button(root, text = "7", width = 5, height = 1, font = ("Lucida Console", 30, "bold"), bd = 1, fg ="black", bg = "gray", command = lambda: show("7")).place(x = 10, y = 200)
Button(root, text = "8", width = 5, height = 1, font = ("Lucida Console", 30, "bold"), bd = 1, fg ="black", bg = "gray", command = lambda: show("8")).place(x = 150, y = 200)
Button(root, text = "9", width = 5, height = 1, font = ("Lucida Console", 30, "bold"), bd = 1, fg ="black", bg = "gray", command = lambda: show("9")).place(x = 290, y = 200)
Button(root, text = "-", width = 5, height = 1, font = ("Lucida Console", 30, "bold"), bd = 1, fg ="black", bg = "gray", command = lambda: show("-")).place(x = 430, y = 200)


Button(root, text = "4", width = 5, height = 1, font = ("Lucida Console", 30, "bold"), bd = 1, fg ="black", bg = "gray", command = lambda: show("4")).place(x = 10, y = 300)
Button(root, text = "5", width = 5, height = 1, font = ("Lucida Console", 30, "bold"), bd = 1, fg ="black", bg = "gray", command = lambda: show("5")).place(x = 150, y = 300)
Button(root, text = "6", width = 5, height = 1, font = ("Lucida Console", 30, "bold"), bd = 1, fg ="black", bg = "gray", command = lambda: show("6")).place(x = 290, y = 300)
Button(root, text = "+", width = 5, height = 1, font = ("Lucida Console", 30, "bold"), bd = 1, fg ="black", bg = "gray", command = lambda: show("+")).place(x = 430, y = 300)


Button(root, text = "1", width = 5, height = 1, font = ("Lucida Console", 30, "bold"), bd = 1, fg ="black", bg = "gray", command = lambda: show("1")).place(x = 10, y = 400)
Button(root, text = "2", width = 5, height = 1, font = ("Lucida Console", 30, "bold"), bd = 1, fg ="black", bg = "gray", command = lambda: show("2")).place(x = 150, y = 400)
Button(root, text = "3", width = 5, height = 1, font = ("Lucida Console", 30, "bold"), bd = 1, fg ="black", bg = "gray", command = lambda: show("3")).place(x = 290, y = 400)
Button(root, text = "0", width = 10, height = 1, font = ("Lucida Console", 30, "bold"), bd = 1, fg ="black", bg = "gray", command = lambda: show("0")).place(x = 10, y = 500)


Button(root, text = ".", width = 5, height = 1, font = ("Lucida Console", 30, "bold"), bd = 1, fg ="black", bg = "gray", command = lambda: show(".")).place(x = 290, y = 500)
Button(root, text = "=", width = 5, height = 3, font = ("Lucida Console", 30, "bold"), bd = 1, fg ="black", bg = "gray", command = lambda: calculate()).place(x = 430, y = 400)


root.mainloop()