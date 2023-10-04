from tkinter import *
from googletrans import Translator, LANGUAGES
from tkinter import ttk
root=Tk()
root.geometry("1080x500")
root.resizable(0,0)
root.config(bg="skyblue")
root.title("EASY Language_Translator")

root.iconbitmap("C:\\Users\\Eng_Mus\\Desktop\\EasyLang_Translator\\elt.ico")

def reset_fields():
    Input_text.delete(1.0, END)
    output.delete(1.0,END)


def Translate():
    translator = Translator()
    translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lan.get())

    output.delete(1.0, END)
    output.insert(END, translated.text)

 


f2=Frame(root, borderwidth=8, bg="white", relief=SUNKEN)
f2.pack(side="top", fill="x")
l=Label(f2, text="EASY LANGUAGE TRANSLATOR",font=("Times New Roman", 20, "bold"), bg="white")
l.pack(pady=10)

f3=Frame(root, borderwidth=8, bg="white smoke", relief=SUNKEN)
f3.pack(side="bottom", fill="x")


#Label(root, text = "TRANSLATOR", bg="white smoke", font=("Times New Roman", 20, "bold")).pack(pady=10)
#fr=Label(f3,text ="Every Language Translator", bg = "white smoke", font =( "Times New Roman", 15, "bold") , width = '20')
#fr.pack(pady=10,side = 'bottom')

Label(root, text="Enter Text", font=("Times New Roman",17, "bold"), bg="skyblue", fg="black").place(x=17, y=120)
#Label(root, text="Enter Text", font=("Times New Roman",13, "bold"), bg="White smoke").place(x=200, y=60)


#input lable defining

Input_text = Text(root, font =("Times New Roman", 15,"bold"), height = 11, wrap = WORD, padx=5, pady=5, width = 45)
Input_text.place(x=15, y=170)

#output lable defining
Label(root, text="Translation", font=("Times New Roman",17,"bold"),bg="skyblue", fg="black").place(x=600, y=120)
#entry of output
output = Text(root,font =("Times New Roman", 15,"bold"), height = 11, wrap = WORD, padx=5, pady=5, width = 45)
output.place(x=600, y=170)

#chose input languges
language=list(LANGUAGES.values())
src_lang =ttk.Combobox(root, values= language, width =22, height=23, font=("Times New Roman", 14 ))
src_lang.place(x=260,y=120)
src_lang.set('English')

#chose output langugaes
dest_lan =ttk.Combobox(root, values= language, width =22, height=23, font=("Times New Roman", 14 ))
dest_lan.place(x=840,y=120)
dest_lan.set('Sindhi')

#creating button
trans_btn = Button(root, text = 'Translate',font = ("Times New Roman" ,12, "bold") ,pady = 5,command = Translate , bg = 'red', activebackground = 'Yellow')

trans_btn.place(x = 500, y= 230 )
#button used for clearing the boards
cr= Button(root, text="Reset",command=reset_fields, font = ("Times New Roman" ,12, "bold") ,pady = 5, bg = 'red', activebackground = 'Yellow')
cr.place(x = 515, y= 320 )






root.mainloop()