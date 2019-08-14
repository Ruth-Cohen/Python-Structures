# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 14:41:03 2018

@author: spanier
"""
import random
   # print random.randint(3, 9)
import math
#from myboolfuncs import 

    
   
def Reshuma(N):
    tup=()
    for i in range(N):
        T1= random.randint(3, 9)
        tup +=  (T1,)
    print(tup)
    return tup

def MyGuess(N1):
    myGuess=[]
    for j in range(N1):
         guess =  input("Try to guess the numbers between 1-9! :")
         myGuess.append(guess)
    for i in myGuess:
        print(i)
    return myGuess

def nihushTest(r,g,num):
    result=()
    success=0
    for i in range(num):
        if r[i]==g[i]:
            item=r[i]
            result= result+item
            success+=1
        else:
            result= result + ("X",)
    p= success/num
    percent= p*100
    print(result, end=" ")
    print (percent)
    return
    


while True:
     num = int(input("How many digits do you want to guess (press -1 to quit):"))
     if num == -1:
         break
     else:
         reshuma= Reshuma(num)
         guessList= MyGuess(num) 
         nihushTest(reshuma,guessList,num)