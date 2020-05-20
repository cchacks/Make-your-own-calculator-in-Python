from tkinter import *
from tkinter import messagebox

a=Tk()
a.resizable(0,0)
var=StringVar()

edit=Entry(a,textvariable=var)
edit.grid(row=0,column=0,columnspan=4)

def insert(op):
	current_str=var.get()
	updated_str=current_str+op
	var.set(updated_str)

def calculate():
	try:
		current_str=var.get()
		# eval() is a built in function
		# takes a string and evaluate the string
		result=eval(current_str)
		var.set(result)
	except:
		messagebox.showerror('Error',"Please check your input")

# buttons

btn7=Button(a,text="7",command=lambda:insert("7"))
btn7.grid(row=1,column=0)
btn8=Button(a,text="8",command=lambda:insert("8"))
btn8.grid(row=1,column=1)
btn9=Button(a,text="9",command=lambda:insert("9"))
btn9.grid(row=1,column=2)
btn_plus=Button(a,text="+",command=lambda:insert("+"))
btn_plus.grid(row=1,column=3)


btn4=Button(a,text="4",command=lambda:insert("4"))
btn4.grid(row=2,column=0)
btn5=Button(a,text="5",command=lambda:insert("5"))
btn5.grid(row=2,column=1)
btn6=Button(a,text="6",command=lambda:insert("6"))
btn6.grid(row=2,column=2)
btn_miuns=Button(a,text="-",command=lambda:insert("-"))
btn_miuns.grid(row=2,column=3)


btn1=Button(a,text="1",command=lambda:insert("1"))
btn1.grid(row=3,column=0)
btn2=Button(a,text="2",command=lambda:insert("2"))
btn2.grid(row=3,column=1)
btn3=Button(a,text="3",command=lambda:insert("3"))
btn3.grid(row=3,column=2)
btn_mul=Button(a,text="*",command=lambda:insert("*"))
btn_mul.grid(row=3,column=3)


btn0=Button(a,text="0",command=lambda:insert("0"))
btn0.grid(row=4,column=0)
btn_dot=Button(a,text=".",command=lambda:insert("."))
btn_dot.grid(row=4,column=1)
btn_eq=Button(a,text="=",command=calculate)
btn_eq.grid(row=4,column=2)
btn_div=Button(a,text="/",command=lambda:insert("/"))
btn_div.grid(row=4,column=3)




a.mainloop()