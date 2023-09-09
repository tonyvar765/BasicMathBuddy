from tkinter import *
root=Tk()
root.geometry("312x324")
root.resizable(0, 0)
root.title("CALCULATOR")
expression=""
input_text=StringVar()
def btn_click(item):
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


input_frame = Frame(root, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)

input_field = Entry(input_frame,font=('arial',18,'bold'),textvariable=input_text,width=50,bg="#eee", bd=0,justify= RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady= 10)

btns_frame = Frame(root,width=132,height=272.5, bg="grey")
btns_frame.pack()

clear = Button(btns_frame,text="clear",fg="black",width = 32,height=3,bd=0,bg="#eee",cursor="hand2", command=lambda: btn_clear()).grid(row=0,column=0,columnspan=3,padx=1,pady=1)
divide = Button(btns_frame,text="/",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command= lambda:btn_click("/")).grid(row=0,column=3,padx=1,pady=1)








root.mainloop()




