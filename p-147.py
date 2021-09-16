from tkinter import *
from tkmacosx import *

root=Tk()
root.title("ASCII")
root.geometry("400x400")
root.configure(background = "red")

label1=Label(root,text="ASCII convertor")
label1.place(relx=0.5,rely=0.2,anchor=CENTER)

text_input=Entry(root)
text_input.place(relx=0.5,rely=0.4,anchor=CENTER) 

label2=Label(root,text="Name in ASCII:")
label3=Label(root,text="Encrypted name:")

def Ascii_convertor():
    input_word=text_input.get()
    for letter in input_word:
        label2["text"]+=str(ord(letter))+" "
        ascii=ord(letter)-1
        label3["text"]+=str(chr(ascii))


button=Button(root,text="Show text in ASCII",command=Ascii_convertor,bg='blue',fg='light green')
button.place(relx=0.5,rely=0.6,anchor=CENTER)
label2.place(relx=0.5,rely=0.8,anchor=CENTER)
label3.place(relx=0.5,rely=0.9,anchor=CENTER)

root.mainloop()
