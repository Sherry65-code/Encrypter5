# Created by Parambir Singh
# Open-Source
from ast import Delete
from tkinter import Tk, PhotoImage, Text, Button, messagebox
from os import system,remove
from pyperclip import copy
algo = 1

def tell(head, text):
    messagebox.showinfo(f'{head}',f"{text}")

def encrypt():
    global algo
    textofbox = textbox.get("1.0","end")
    textofbox = textofbox.replace(" ","_")
    try:
        remove("text.algo")
    except Exception as e:
        print("Could not remove text.algo")
    f = open("text.algo","w")
    f.write(f"{textofbox}")
    f.close()
    if algo == 1:
        system("./encrypter.out")
    tell("Encrypted","Text Copied to clipboard.")
    f = open("text.algo","r")
    txt = f.read()
    f.close()
    copy(f"{txt}")

def descrypt():
    global algo
    textofbox=textbox.get("1.0","end")
    try:
        remove("text.algo")
    except Exception as e:
        print("Could not remove text.algo")
    f = open("text.algo","w")
    f.write(f"{textofbox}")
    f.close()
    if algo == 1:
        system("./decrypter.out")
    f = open("text.algo","r")
    txt = f.read()
    f.close()
    copy(f"{txt.replace('_',' ')}")
    tell("Decrypted",f"{txt.replace('_',' ')}")


def setcode():
    tell("Listen","Only Algorithm A217 is avaliable for now.")

def about():
    tell("About Us","This is a program that encrypts and descrypts text without use of special characters")
root = Tk()
root.title("Encrypter 5")
root.geometry("400x300")
root.config(bg="#31363b")
root.resizable(0,0)
root.iconphoto(False, PhotoImage(file='icon.png'))
fontname="Ubuntu"
fontsize=10
fontmain=(f"{fontname}",fontsize)
textbox = Text(width=36, height=15, borderwidth=0, relief="flat", highlightthickness=0,bg="#bababa")
textbox.place(x=20, y=20)
lockimg = PhotoImage(file=r"lock.png")
unlockimg = PhotoImage(file=r"unlock.png")
codeimg = PhotoImage(file=r"code.png")
infoimg = PhotoImage(file=r"info.png")
Button(image=lockimg, relief="flat", borderwidth=0, highlightthickness=0,bg="#31363b", command=encrypt).place(x=330, y=20)
Button(image=unlockimg, relief="flat", borderwidth=0, highlightthickness=0,bg="#31363b", command=descrypt).place(x=330, y=90)
Button(image=codeimg, relief="flat", borderwidth=0, highlightthickness=0,bg="#31363b", command=setcode).place(x=330, y=160)
Button(image=infoimg, relief="flat", borderwidth=0, highlightthickness=0,bg="#31363b",command=about).place(x=330, y=230)
root.mainloop()