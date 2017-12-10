from tkinter import *

root =Tk()#створення вікна
root.title('* & /')
root.geometry('240x150')

def View(event):
     v = var.get()
     number1,number2 = EntryFirst.get(),EntrySecond.get()
     validation(number1,number2,v)

def validation(number1,number2,v):
    if number1 == '':
        ResultFirst['text'] = 'Заповніть всі поля'
    if number2 == '':
         ResultSecond['text'] = 'Заповніть всі поля'
    if number1 != '' and number2 != '':
        if v == 1:
            divide(float(number1),float(number2))
        elif v == 0:
            multiply(float(number1),float(number2))

def multiply(number1,number2):
    result = number1*number2
    ResultFirst['text'] = result

def divide(number1,number2):
    if number2 == 0:
        ResultSecond['text'] = 'num2 == 0' 
    elif number2 != 0:
        result = number1/number2
        ResultSecond['text'] = result  


FirstNumber = Label(root, text ="Перше число:", fg = "black")
EntryFirst = Entry(root)
SecondNumber = Label(root, text ="Друге число:", fg = "black") 
EntrySecond = Entry(root)
ResultFirst = Label(root, text ="-//-", fg = "black")
ResultSecond = Label(root, text ="-//-", fg = "black")

FirstNumber.grid (row=0, sticky = E)
SecondNumber.grid (row=1, sticky = E)

EntryFirst.grid (row=0, column=1)
EntrySecond.grid (row=1, column=1)


var=IntVar()
var.set(0)
radio1 = Radiobutton (root, text = "Помножити",variable=var, value = 0)
radio1.grid (columnspan=1,row = 3)
ResultFirst.grid(row =3,column =1)
radio2 = Radiobutton (root, text = "Поділити",variable=var, value = 1)
radio2.grid (columnspan=1)
ResultSecond.grid(row =4,column =1)

button1 = Button (root, text ="Обчислити")
button1.bind('<Button-1>',View) 
button1.grid (columnspan = 2)

root.mainloop()