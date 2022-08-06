# Created by Parambir Singh
# Open-Source
from tkinter import Tk, PhotoImage, Text, Button, messagebox

def tell(head, text):
    messagebox.showinfo(f'{head}',f"{text}")

def encrypt():
    pass

def descrypt():
    pass

def setcode():
    pass

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