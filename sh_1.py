# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def TOlist(L):
    lst=[]
    for item in L:
        if isinstance (item,tuple):
            for value in item:
                lst.append(value)
    #print(lst)
    return lst    
        
def ToTuple(T):
    tup=()
    for item in T:
        if isinstance (item,list):
               T1=tuple(item)
               tup= tup+T1
    #print(tup)
    return tup    

def listOfStrings(LS):
    L1=[]
    for item in LS:
        if isinstance (item,str):
            for value in item:
               if checkIfExist(LS, value):
                    L1.append(value)
    #print(L1)
    return L1  

def listOfNums(LN):
    L2=[]
    for item in LN:
        if isinstance (item, int or float):
            if checkIfExist(LN, item):
              L2.append(item)
    #print(L2)
    return L2

def checkIfExist(lst,val):
    checkList=TOlist(lst)
    checkTuple=ToTuple(lst)
    for i in checkList:
        if val==i:
            return False
    for j in checkTuple:
        if val==j:
            return False
        
    return True 
        
        
        
        
        
        
        
        
        
        
        
        
        
        