from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint
maingame =Tk()
maingame.title("TIC TAC TOE")
maingame.configure(background = '#FA5858')
activePlayer = 1
listPlayer1 = []
listPlayer2 = []
computerList = []
comupterPlayed = []
gamemode = 0
def setplayer(n):
   global gamemode
   if(n==1):
      gamemode = 1
   elif (n==2):
      gamemode = 2
   
# Start Select PLayer Section
choose1 = Button(maingame,text = "One Player",foreground="#2E2E2E",background="#A9F5F2",font="Aerial 12")
choose1.config(command=lambda : setplayer(1))
choose1.grid(row = 0,column = 0,padx=(35, 35),pady=(30, 30),ipady=10,ipadx=10)
choose2 = Button(maingame,text = "Two Players",foreground="#2E2E2E",background="#58FAF4",font="Aerial 12")
choose2.config(command=lambda : setplayer(2))
choose2.grid(row = 0,column = 2,padx=(35, 35),pady=(30, 30),ipady=10,ipadx=10)
# End Select PLayer Section

# Start Buttton Section
but1 = Button(maingame,text = " ",background="#FFFFFF",font="Times 16")
but1.config(command=lambda : makeChange(1))
but1.grid(row=1,column=0,padx=(40, 40),pady=(30, 30),ipady=40,ipadx=40)

but2 = Button(maingame,text = " ",background="#FFFFFF",font="Times 16")
but2.config(command=lambda : makeChange(2))
but2.grid(row=1,column=1,padx=(40, 40),pady=(30, 30),ipady=40,ipadx=40)

but3 = Button(maingame,text = " ",background="#FFFFFF",font="Times 16")
but3.config(command=lambda : makeChange(3))
but3.grid(row=1,column=2,padx=(40, 40),pady=(30, 30),ipady=40,ipadx=40)

but4 = Button(maingame,text = " ",background="#FFFFFF",font="Times 16")
but4.config(command=lambda : makeChange(4))
but4.grid(row=2,column=0,padx=(40, 40),pady=(30, 30),ipady=40,ipadx=40)

but5 = Button(maingame,text = " ",background="#FFFFFF",font="Times 16")
but5.config(command=lambda : makeChange(5))
but5.grid(row=2,column=1,padx=(40, 40),pady=(30, 30),ipady=40,ipadx=40)

but6 = Button(maingame,text = " ",background="#FFFFFF",font="Times 16")
but6.config(command=lambda : makeChange(6))
but6.grid(row=2,column=2,padx=(40, 40),pady=(30, 30),ipady=40,ipadx=40)

but7 = Button(maingame,text = " ",background="#FFFFFF",font="Times 16")
but7.config(command=lambda : makeChange(7))
but7.grid(row=3,column=0,padx=(40, 40),pady=(30, 30),ipady=40,ipadx=40)

but8 = Button(maingame,text = " ",background="#FFFFFF",font="Times 16")
but8.config(command=lambda : makeChange(8))
but8.grid(row=3,column=1,padx=(40, 40),pady=(30, 30),ipady=40,ipadx=40)

but9 = Button(maingame,text = " ",background="#FFFFFF",font="Times 16")
but9.config(command=lambda : makeChange(9))
but9.grid(row=3,column=2,padx=(40, 40),pady=(30, 30),ipady=40,ipadx=40) 
# End Buttton Sections

# Start Select Comupter or Players Section
def makeChange(place):
   global activePlayer
   if (gamemode==1):
      if (activePlayer==1):  
         activePlayer=2
         maingame.title("TIC TAC TOY : Player 1")
         changeButton(place,'X')
         listPlayer1.append(place) 
         Computer()
         winner_computer()
      elif (activePlayer==2):
         activePlayer=1
         maingame.title("TIC TAC TOY : Player 1")
         changeButton(place,'O')
         listPlayer2.append(place)
         
     
   elif (gamemode==2):
      if (activePlayer==1):  
         activePlayer=2
         maingame.title("TIC TAC TOY : Player 1")
         changeButton(place,'X')
         listPlayer1.append(place) 
      elif (activePlayer==2):
         activePlayer=1
         maingame.title("TIC TAC TOY : Player 2")
         changeButton(place,'O')
         listPlayer2.append(place)
      winner()      
def Computer():
   global listPlayer1
   global listPlayer2
   global comupterPlayed
   computerList = []
   for i in range(9):
      if not(i+1 in listPlayer1 or i+1 in listPlayer2):
         computerList.append(i+1)
   if(len(computerList)>1):
      randindex = randint(0,len(computerList)-1)
      comupterPlayed.append(computerList[randindex])
      makeChange(computerList[randindex])
# End Select Comupter or Players Section

#Start Winner Section
def winner_computer():
   winner_computer=0
   global comupterPlayed
   global listPlayer1
   #Game_Rule
   if 1 in comupterPlayed and 2 in comupterPlayed and 3 in comupterPlayed:
      winner_computer = 1
   elif 4 in comupterPlayed and 5 in comupterPlayed and 6 in comupterPlayed:
      winner_computer = 1
   elif 1 in comupterPlayed and 5 in comupterPlayed and 9 in comupterPlayed:
      winner_computer = 1
   elif 3 in comupterPlayed and 5 in comupterPlayed and 7 in comupterPlayed:
      winner_computer = 1   
   elif 7 in comupterPlayed and 8 in comupterPlayed and 9 in comupterPlayed:
      winner_computer = 1
   elif 1 in comupterPlayed and 4 in comupterPlayed and 7 in comupterPlayed:
      winner_computer = 1
   elif 2 in comupterPlayed and 5 in comupterPlayed and 8 in comupterPlayed:
      winner_computer = 1
   elif 3 in comupterPlayed and 6 in comupterPlayed and 9 in comupterPlayed:
      winner_computer = 1
   elif 1 in listPlayer1 and 2 in listPlayer1 and 3 in listPlayer1:
      winner_computer = 2
   elif 4 in listPlayer1 and 5 in listPlayer1 and 6 in listPlayer1:
      winner_computer = 2
   elif 1 in listPlayer1 and 5 in listPlayer1 and 9 in listPlayer1:
      winner_computer = 2
   elif 3 in listPlayer1 and 5 in listPlayer1 and 7 in listPlayer1:
      winner_computer = 2   
   elif 7 in listPlayer1 and 8 in listPlayer1 and 9 in listPlayer1:
      winner_computer = 2
   elif 1 in listPlayer1 and 4 in listPlayer1 and 7 in listPlayer1:
      winner_computer = 2
   elif 2 in listPlayer1 and 5 in listPlayer1 and 8 in listPlayer1:
      winner_computer = 2
   elif 3 in listPlayer1 and 6 in listPlayer1 and 9 in listPlayer1:
      winner_computer = 2   
   if (winner_computer==1):
      messagebox.showinfo(title="Winner",message="Compuer")
      maingame.destroy()
   elif (winner_computer==2):
      messagebox.showinfo(title="Winner",message="Player 1") 
      maingame.destroy()
   if (len(listPlayer1)==5 and winner_computer==0 and len(comupterPlayed)==4):
      messagebox.showinfo(title="NO winner",message="Draw")  
      maingame.destroy()
def winner():
   winner = 0
   #Game_Rule
   if 1 in listPlayer1 and 2 in listPlayer1 and 3 in listPlayer1:
      winner = 1
   elif 4 in listPlayer1 and 5 in listPlayer1 and 6 in listPlayer1:
      winner = 1
   elif 3 in listPlayer1 and 5 in listPlayer1 and 7 in listPlayer1:
      winner = 1
   elif 1 in listPlayer1 and 5 in listPlayer1 and 9 in listPlayer1:
      winner = 1      
   elif 7 in listPlayer1 and 8 in listPlayer1 and 9 in listPlayer1:
      winner = 1
   elif 1 in listPlayer1 and 4 in listPlayer1 and 7 in listPlayer1:
      winner = 1
   elif 2 in listPlayer1 and 5 in listPlayer1 and 8 in listPlayer1:
      winner = 1
   elif 3 in listPlayer1 and 6 in listPlayer1 and 9 in listPlayer1:
      winner = 1
   elif 1 in listPlayer2 and 2 in listPlayer2 and 3 in listPlayer2:
      winner = 2
   elif 4 in listPlayer2 and 5 in listPlayer2 and 6 in listPlayer2:
      winner = 2
   elif 7 in listPlayer2 and 8 in listPlayer2 and 9 in listPlayer2:
      winner = 2
   elif 1 in listPlayer2 and 4 in listPlayer2 and 7 in listPlayer2:
      winner = 2
   elif 2 in listPlayer2 and 5 in listPlayer2 and 8 in listPlayer2:
      winner = 2
   elif 3 in listPlayer2 and 6 in listPlayer2 and 9 in listPlayer2:
      winner = 2  
   if (winner==1):
      messagebox.showinfo(title="Winner",message="Player 1")
      maingame.destroy()
   elif (winner==2):
      messagebox.showinfo(title="Winner",message="Player 2")
      maingame.destroy()
   if len(listPlayer2)==4 and winner==0 and len(listPlayer1)==5:
      messagebox.showinfo(title="NO winner",message="Draw")
      maingame.destroy()
#End Winner Section

# Start Set Changed Played Section
def changeButton(place,text):
   if (place==1):
      but1.config(text=text,state=DISABLED)
   elif (place==2):
      but2.config(text=text,state=DISABLED)
   elif (place==3):
      but3.config(text=text,state=DISABLED)
   elif (place==4):
      but4.config(text=text,state=DISABLED)
   elif (place==5):
      but5.config(text=text,state=DISABLED)
   elif (place==6):
      but6.config(text=text,state=DISABLED)
   elif (place==7):
      but7.config(text=text,state=DISABLED)
   elif (place==8):
      but8.config(text=text,state=DISABLED)
   elif (place==9):
      but9.config(text=text,state=DISABLED)
# Start Set Changed Played Section
maingame.mainloop()
