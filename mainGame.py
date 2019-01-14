import random
import sys
import time
import tkinter

hp=100
iq=0
i=0
j=0
n = 10
timeleft = 0
status = ""
status1 = ""
s1 = 0
s2 = 0
Xs = range(50)

start_time=time.time()

def startGame(event): 
     if timeleft == 0:
         countdown()
     Forward(iq,hp)

def Display(i,j):
  pos.config(text ="You are at: ["+str(i)+","+str(j)+"]")
  
def countdown(): 
    global hp, timeleft 
    if timeleft >= 0: 
  
        timeleft += 1
        if timeleft%5==0:
            hp-=1
            
       
        timeLabel.config(text = "Time left: "
                               + str(timeleft)) 
        
        hpp.config(text = "HP: " + str(hp)) 	
                                 
     
        timeLabel.after(1000, countdown) 
   

def AskQues():
    global s1,s2, status, status1, timediff, hp, iq
  
    if hp>0:
        Display(i,j)
        e.focus_set() 

        if e.get().strip() == str(s1+s2): 
            hp += 1
            iq +=1
            status = "ANS IS CORRECT"
            e1.focus_set()
        if e1.get().strip() == str(s1*s2): 
            hp += 1
            iq +=1
            status1 = "ANS IS CORRECT"
            e2.focus_set()
        elif (e1.get().strip()!=''):
            hp -= 5
            iq -=1
            status1 = "ANS IS WRONG"
            e2.focus_set()
        elif (e.get().strip()!=''):
            hp -= 5
            iq -=1
            status = "ANS IS WRONG"
            e1.focus_set()
        if e1.get().strip() == str(s1*s2): 
            hp += 1
            iq +=1
            status1 = "ANS IS CORRECT"
            e2.focus_set()  
        elif (e1.get().strip()!=''):
            hp -= 5
            iq -=1
            status1 = "ANS IS WRONG"
            e2.focus_set()  
          
        stat.config(text = status)
        stat1.config(text = status1)
        e.delete(0, tkinter.END) 
        e1.delete(0,tkinter.END)
        s1 = random.choice(Xs)
        s2 = random.choice(Xs)
        label.config(text = str(s1)+" + " +str(s2)) 
        label2.config(text = str(s1)+" x " +str(s2)) 
        hpp.config(text = "HP: " + str(hp)) 	
        iqq.config(text = "IQ: " + str(iq)) 	

def checkmax():
    global i,j
    if i>9:
        i=9
        wall=tkinter.Label(root, text="Ya hit a wall!")
        pos.config(text ="You are at: ["+str(i)+","+str(j)+"]")
        wall.grid(row=9,column=0)
    if j>9:
        j=9
        wall=tkinter.Label(root, text="Ya hit a wall!")
        pos.config(text ="You are at: ["+str(i)+","+str(j)+"]")
        wall.grid(row=9,column=0)
    
def checkmin():
    global i,j
    if i<0:
        i=0
        wall=tkinter.Label(root, text="Ya hit a wall!")
        pos.config(text ="You are at: ["+str(i)+","+str(j)+"]")
        wall.grid(row=9,column=0)
    if j<0:
        j=0
        wall=tkinter.Label(root, text="Ya hit a wall!")
        pos.config(text ="You are at: ["+str(i)+","+str(j)+"]")
        wall.grid(row=9,column=0)

def Advance(dir):
    e2.delete(0,tkinter.END)
    global i,j
    print (dir)
    if dir=='R':
        j+=1
        checkmax()
    elif dir=='L':
        j-=1
        checkmin()
    elif dir=='U':
        i-=1
        checkmin()
    elif dir=='D':
        i+=1
        checkmax()
    AskQues()

def Forward(iq,hp):
    global i,j
    Display(i,j)
    
    if i==(n-1) and j==(n-1):
        win=tkinter.Label(root,text="Winner Winner Chicken Dinner", font =('Helvetica', 80))
        win.grid(row=0, rowspan = 10,column=0,columnspan=10)
    else:
            Dir.config(text = "ENTER DIR = ")
            e2.focus_set()
            Advance(e2.get().strip())
    if hp<=0:
        win=tkinter.Label(root,text="ded",font = ('Helvetica', 200))
        win.grid(row=0, rowspan = 10,column=0,columnspan=10)
      

root = tkinter.Tk() 
  
root.title("NERDY_MATH_GAME") 
  
root.geometry("700x700") 
  
instructions = tkinter.Label(root, text = "NERDY_MATH_GAME", 
                                      font = ('Helvetica', 20)) 
instructions.grid(row=0,column= 0, columnspan=2)
  
scoreLabel = tkinter.Label(root, text = "Press enter to start", 
                                      font = ('Helvetica', 12)) 
scoreLabel.grid(row = 1, column= 1, columnspan = 25) 
  
timeLabel = tkinter.Label(root, text = "Time elapsed: " +
              str(timeleft), font = ('Helvetica', 12)) 
                
timeLabel.grid(row = 1, column=0)
  
label = tkinter.Label(root, text = "______" ,font = ('Helvetica', 12)) 
label.grid(row = 2, column = 4) 

label2 = tkinter.Label(root,text = "______" , font = ('Helvetica', 12)) 
label2.grid(row = 4, column = 4)

plus =tkinter.Label(root, text = "=", font = ('Helvetica', 12))
plus.grid(row=4, column=5) 
  
Dir =tkinter.Label(root, text = "DIR =", font = ('Helvetica', 16))
Dir.grid(row=2, column=0) 
e = tkinter.Entry(root) 
e1 = tkinter.Entry(root) 
e2 = tkinter.Entry(root) 
plus =tkinter.Label(root, text = "=", font = ('Helvetica', 12))
plus.grid(row=2, column=5)
stat = tkinter.Label(root, text = "", font = ('Helvetica', 12))
stat.grid(row=3, column=3)
stat1 = tkinter.Label(root, text = "", font = ('Helvetica', 12))
stat1.grid(row=5, column=3)
pos = tkinter.Label(text = "Start position",font = ('Helvetica', 12))
pos.grid(row = 7, column = 1)
hpp = tkinter.Label(root, text = "HP = ", font = ('Helvetica', 12))
hpp.grid(row = 7, column = 0)
iqq = tkinter.Label(root, text = "IQ = ", font = ('Helvetica', 12))
iqq.grid(row = 8, column = 0)
root.bind('<Return>',startGame) 
e.grid(row = 2, column = 6) 
e1.grid(row = 4, column = 6) 
e2.grid(row=2,column=1)
  

e.focus_set() 
e1.focus_set()
e2.focus_set()
root.mainloop() 
