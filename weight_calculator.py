from tkinter import *    #importing some specific libraries from module

window=Tk()

window.title("Weight Calculator using python")

def from_kg():      #defining main function
    Gram = float(user_value.get()) * 1000
    Pound= float(user_value.get()) * 2.20462
    Ounce = float(user_value.get()) * 35.274
#inserting text into textboxes
    textbox1.delete("1.0", END)
    textbox1.insert(END, Gram)

    textbox2.delete("1.0", END)
    textbox2.insert(END, Pound)

    textbox3.delete("1.0", END)
    textbox3.insert(END, Ounce)

# creating windows for layout
e1=Label (window,text="Enter weight in kg")
user_value=StringVar()  #user_value is a variable defined here
e2 =Entry(window,textvariable=user_value)
e3=Label(window,text='Gram')
e4=Label(window,text='Pound')
e5=Label(window,text='Ounce')

 #providing size for our textboxes
textbox1= Text(window,height=1,width=20)
textbox2= Text(window,height=1,width=20)
textbox3= Text(window,height=1,width=20)

#creating a button
b1=Button(window,text="Convert",command=from_kg)

#giving position for placement to the boxes
e1.grid(row=0,column=0)
e2.grid(row=0,column=1)
e3.grid(row=1,column=0)
e4.grid(row=1,column=1)
e5.grid(row=1,column=2)
textbox1.grid (row=2,column=0)
textbox2.grid (row=2,column=1)
textbox3.grid (row=2,column=2)
b1.grid (row=0,column=2)



window.mainloop()