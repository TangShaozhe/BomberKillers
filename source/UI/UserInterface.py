from tkinter import *
from tkinter.font import BOLD
root = Tk()
root.title("Main Window")
root.minsize(height=540,width=720)
root.config(bg="slategray")
img = PhotoImage("bg.jpg")

label1 = Label(root,image=img,text="BomberManKiller",font=('Arial',25))
label1.pack()
def playgame():
    print("Welcome Play the Game")
def tryagain():
    print("Try again")
def playwithBot():
    print("Play with Bot")
def showIntruction():
    root = Tk()
    root.title("Instruction")
    root.minsize(height=400,width=400)
    label2 = Label(root,text="Instruction",font=("Arial",20))
    label2.pack()
    button = Button(root,height=1,width=15,text='Go Back', fg='maroon',command=exit,activebackground="teal",bd=2,font='arial 14 bold')
    button.pack()
    button.place(x=200, y=350)
    root.mainloop()

button1 = Button(root,height=1,width=15,text='PlayGame', fg='maroon',command=playgame,activebackground="teal",bd=2,font='arial 14 bold')
button1.pack()
button1.place(x=200, y=100)
button2 = Button(root,height=1,width=15,text='TryAgain',fg='maroon',command=tryagain,activebackground="teal",bd=2,font='arial 14 bold')
button2.pack()
button2.place(x=200, y=140)
button3 = Button(root,height=1,width=15,text='Play with Bot',fg='maroon',command=playwithBot,activebackground="teal",bd=2,font='arial 14 bold')
button3.pack()
button3.place(x=200, y=180)
button4 = Button(root,height=1,width=15,text='Show Instruction',fg='maroon',command=showIntruction,activebackground="teal",bd=2,font='arial 14 bold')
button4.pack()
button4.place(x=200, y=220)
button5 = Button(root,height=1,width=15,text='Exit',fg='maroon',command=exit,activebackground="teal",bd=2,font='arial 14 bold')
button5.pack()
button5.place(x=200, y=260)
root.mainloop()
