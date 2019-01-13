
"""
Spyder Editor

This is a temporary script file.
"""
import random
import sys
import time

hp=100
iq=0

n=int(input("Select degree!"))

i=0
j=0

start_time=time.time()


def Display(i,j):
    print("You are at: ["+str(i)+","+str(j)+"]")
    
def AllCalc(q1,q2):
    global start_time, timediff
    global i, j
    global hp,iq
    if q1==True and q2==True:
        iq+=2
        hp+=2
    elif q1==False and q2==False:
        iq-=2
        hp-=10
    else:
        hp-=4
    timediff=int(time.time() - start_time)
    while timediff>0:
        hp-=1
        timediff-=5
        
    Forward(iq,hp)

def CheckAns(Anss,index):
    if Anss is index:
        print("Correct")
        return True
    else:
        print("OOpsie!")
        return False

def AskQues():
    index1 = random.randint(0,100)
    index2 = random.randint(0,16)
    ans1=int(input(str(index1)+"+"+str(index2)+" Answer 1! "))
    ans2=int(input(str(index1)+"*"+str(index2)+" Answer 2! "))
    verdict1 = CheckAns(ans1,(index1+index2))
    verdict2 = CheckAns(ans2,(index1*index2))
    AllCalc(verdict1,verdict2)	

def checkmax():
    global i,j
    if i>=n:
        i-=1
        print("Ya hit a wall!")
    if j>=n:
        j-=1
        print("Ya hit a wall!")
    
def checkmin():
    global i,j
    if i<=0:
        i+=1
        print("Ya hit a wall!")
    if j<=0:
        j+=1
        print("Ya hit a wall!")

def Advance(dir):
    global i,j
    if dir=='R':
        j+=1
        checkmax()
    elif dir=='L':
        j-=j
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
    print("HP="+str(hp))
    print("IQ="+str(iq))
    if i==(n-1) and j==(n-1):
        print("Winner Winner Chicken Dinner")
    else:
        if hp>0 :
            dir=input("Direction")
            Advance(dir)
        else:
            print("Dead")
Forward(iq,hp)