import tkinter,random,time
from tkinter import *
root=Tk()
root.title("ROCK PAPER SCISSOR")
root.configure(bg="lightblue")
blank1,win,lose="                                                        ",0,0
lab3=Label(root,text='ROCK PAPER SCISSOR',font=('algerian',18),background="lightblue").grid(row=1,pady=10,column=1,columnspan=3)
lab4=Label(root,text='      Score CARD      ',font=('arial',14),background="lightgreen").grid(row=2,pady=10,column=2,columnspan=2)
lab5=Label(root,text='  YOU :-  ',font=('arial',14),background="lightblue").grid(row=3,pady=5,column=2)
lab5=Label(root,text=' ROBOT :- ',font=('arial',14),background="lightblue").grid(row=4,pady=5,column=2)
lab6=Label(root,text="Please start the game !",font=('arial',14),background="lightblue").grid(row=6,pady=10,column=1,columnspan=3)
blanklab1=Label(root,text=blank1,font=('arial',18),background="white").grid(row=7,pady=14,padx=20,column=1,columnspan=3)
blanklab2=Label(root,text=blank1,font=('arial',18),background="white").grid(row=8,pady=5,padx=20,column=1,columnspan=3)

def strt():
    global win,lose
    blanklab1=Label(root,text=blank1,font=('arial',18),background="white").grid(row=7,pady=14,padx=20,column=1,columnspan=3)
    blanklab2=Label(root,text=blank1,font=('arial',18),background="white").grid(row=8,pady=5,padx=20,column=1,columnspan=3)
    lab6=Label(root,text='      GAME STARTED !!       ',font=('algerian',14),background="lightblue").grid(row=6,pady=10,column=1,columnspan=3)
    win,lose=0,0
    winlab=Label(root,text=win,font=('arial',15),background="lightblue").grid(row=3,pady=5,padx=20,column=3)
    loselab=Label(root,text=lose,font=('arial',15),background="lightblue").grid(row=4,pady=5,padx=20,column=3)

def play(y):
    global win,lose
    x=random.randint(1,3)           #1-rock, 2-paper, 3-scissor
    if x==1:
        blanklab2=Label(root,text=" ROBOT: ROCK 🪨 ",font=("arial",14),background="white").grid(row=8,pady=14,padx=20,column=1,columnspan=3)   
        if y==1:
            lab6=Label(root,text='            DRAW !!            ',font=('arial',14),background="lightblue").grid(row=6,pady=10,column=1,columnspan=3)
        elif y==2:
            lab6=Label(root,text='           YOU WIN !!          ',font=('arial',14),background="lightblue").grid(row=6,pady=10,column=1,columnspan=3)
            win+=1;
        elif y==3:
            lab6=Label(root,text='           YOU LOSE !!         ',font=('arial',14),background="lightblue").grid(row=6,pady=10,column=1,columnspan=3)
            lose+=1;
    elif x==2:
        blanklab2=Label(root,text=" ROBOT: PAPER 📜 ",font=("arial",14),background="white").grid(row=8,pady=14,padx=20,column=1,columnspan=3)
        if y==1:
            lab6=Label(root,text='           YOU LOSE !!         ',font=('arial',14),background="lightblue").grid(row=6,pady=10,column=1,columnspan=3)
            lose+=1;
        elif y==2:
            lab6=Label(root,text='             DRAW !!           ',font=('arial',14),background="lightblue").grid(row=6,pady=10,column=1,columnspan=3)
        elif y==3:
            lab6=Label(root,text='           YOU WIN !!          ',font=('arial',14),background="lightblue").grid(row=6,pady=10,column=1,columnspan=3)  
            win+=1;
    elif x==3:
        blanklab2=Label(root,text=" ROBOT: SCISSOR ✂ ",font=('arial',14),background="white").grid(row=8,pady=14,padx=20,column=1,columnspan=3)
        if y==1:
            lab6=Label(root,text='            YOU WIN !!         ',font=('arial',14),background="lightblue").grid(row=6,pady=10,column=1,columnspan=3)
            win+=1;
        elif y==2:
            lab6=Label(root,text='           YOU LOSE !!         ',font=('arial',14),background="lightblue").grid(row=6,pady=10,column=1,columnspan=3)
            lose+=1;
        elif y==3:
            lab6=Label(root,text='             DRAW !!           ',font=('arial',14),background="lightblue").grid(row=6,pady=10,column=1,columnspan=3)
    winlab=Label(root,text=win,font=('arial',15),background="lightblue").grid(row=3,pady=5,padx=20,column=3)
    loselab=Label(root,text=lose,font=('arial',15),background="lightblue").grid(row=4,pady=5,padx=20,column=3)
    
def rock():
    blanklab1=Label(root,text="    YOU:  ROCK  🪨  ",font=("arial",14),background="white").grid(row=7,pady=5,column=1,columnspan=3)
    play(1)
def paper():
    blanklab1=Label(root,text="  YOU:  PAPER  📜  ",font=("arial",14),background="white").grid(row=7,pady=5,column=1,columnspan=3)
    play(2)
def scissor():
    blanklab1=Label(root,text=" YOU:  SCISSOR  ✂ ",font=('arial',14),background="white").grid(row=7,pady=5,column=1,columnspan=3)
    play(3)

strt=Button(root,text='New Game',font=('arial',12),background="red",bd=3,command=strt).grid(row=2,pady=9,padx=13,column=1)
rck=Button(root,text='Rock 🪨',font=('arial',15),background="yellow",bd=3,command=rock).grid(row=5,pady=9,padx=13,column=1)
papr=Button(root,text='Paper 📜',font=('arial',15),background="yellow",bd=3,command=paper).grid(row=5,pady=9,padx=13,column=2)
scissr=Button(root,text='Scissor ✂',font=('arial',15),background="yellow",bd=3,command=scissor).grid(row=5,pady=9,padx=13,column=3)
credits1=Label(root,text='Developer: Kunal Kashyap',font=('arial',11),background="lightblue").grid(row=9,pady=5,column=1,columnspan=3)
credits2=Label(root,text='© Copylefts Reserved: kkindustries pvt.ltd',font=('arial',11),background="lightblue").grid(row=10,column=1,columnspan=3)
root.geometry("437x470")
root.mainloop()
