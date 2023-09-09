from tkinter import *
root=Tk()
root.geometry("312x324")
root.resizable(0, 0)
root.title("CALCULATOR")
def btn_click():
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression=""
    input_text.set("")

def btn_equal():
    result=str(eval(expression))
    input_text.set(result)
    expression=""
expression=""
input_text=StringVar()

input_frame = Frame(root, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)


root.mainloop()




