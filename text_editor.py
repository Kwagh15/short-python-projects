import tkinter as tk  #tk is petname for tkinter module
from tkinter.filedialog import askopenfilename,asksaveasfilename

def open_file():
    filepath=askopenfilename(
        filetypes=[("Text Files","*.txt"),("All File","*.*")]


    )
    if not filepath:
        return
    txt_edit.delete(1.0,tk.END)
    with open(filepath,"r")as input_file:
        text= input_file.read()
        txt_edit.insert(tk.END,text)
    window.title(f"Text Editor Application by kwagh -{filepath}")

def save_as():
    filepath=asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text files","*.txt"),("All Files","*.*")]

    )
    if not filepath:
        return
    with open(filepath,"w") as output_file:
        text= txt_edit.get(1.0,tk.END)
        output_file.write(text)
    window.title(f"Text Editor Application by Kwagh - {filepath}")



window =tk.Tk()
window.title("Text Editor by kwagh")

#configuration ans specifications of rows and columns
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)


#creating frames
txt_edit = tk .Text(window)
fr_button = tk.Frame(window,relief=tk.RAISED,bd=2)

#creating buttons
btn_open=tk.Button(fr_button,text="Open",command=open_file)
btn_save=tk.Button(fr_button,text="Save as",command=save_as)

#positioning buttons
btn_open.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
btn_save.grid(row=1,column=0,sticky="ew",padx=5)

#positioning frames
fr_button.grid(row=0,column=0,sticky="ns")
txt_edit.grid(row=0,column=1,sticky="nsew")



window.mainloop()
