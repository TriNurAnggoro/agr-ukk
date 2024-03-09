from tkinter import *
import math

def click(value):
    ex = entryField.get()
    answer=''

    try:

        if value=='C':
            ex=ex[0:len(ex)-1]
            entryField.delete(0,END)
            entryField.insert(0,ex)
            return

        elif value=='CE':
            entryField.delete(0,END)

        elif value=='√':
            answer=math.sqrt(eval(ex))

        elif value=='π':
            answer=math.pi

        elif value == 'cos':
            answer = math.cos(math.radians(eval(ex)))

        elif value == 'tan':
            answer = math.tan(math.radians(eval(ex)))

        elif value == 'sin':
            answer = math.sin(math.radians(eval(ex)))

        elif value == "x\u00B3":
            answer = eval(ex) ** 3

        elif value == "x\u00B2":
            answer = eval(ex) ** 2

        elif value == chr(247):
            entryField.insert(END,"/")
            return

        elif value == '=':
            answer = eval(ex)

        else:
            entryField.insert(END,value)
            return

        entryField.delete(0,END)
        entryField.insert(0,answer)
    
    except SyntaxError:
        pass

root=Tk()
root.title("Agr Calculator")
root.config(bg='steelblue')
root.geometry('297x559+370+80')

entryField=Entry(root,font=('arial','20','bold'), bg='steelblue', fg='black',bd=10,relief=SUNKEN,width=18)
entryField.grid(row=0,column=0,columnspan=8)

button_text_list = ["C", "CE", "x\u00B2", "x\u00B3",
                    "sin", "cos", "tan", "√",
                    "1", "2", "3", "+",
                    "4", "5", "6", "-",
                    "7", "8", "9", "*",
                    "%", "0" ,".", chr(247),
                    "(", "π", ")", "="]
rowvalue=1
columnvalue=0
for i in button_text_list:

    button=Button(root,width=5,height=2,bd=4,relief=SUNKEN,text=i,bg='steelblue',fg='black',
              font=('arial',15,'bold'),activebackground='steelblue',command=lambda button=i: click(button))
    button.grid(row=rowvalue,column=columnvalue,pady=1)
    columnvalue+=1
    if columnvalue>3:
        rowvalue+=1
        columnvalue=0

root.mainloop()