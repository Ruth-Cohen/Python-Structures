# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 14:04:12 2018

@author: spanier
"""

def dictionary(L):
    sumTuple=0
    sumList=0
    sumString=0
    sumInt=0
    sumFloat=0
    for item in L:
        if isinstance (item,tuple):
            sumTuple+=1
        if isinstance (item,list):
            sumList+=1
        if isinstance (item,str):
            sumString+=1
        if isinstance (item, int):
            sumInt+=1
        if isinstance (item, float):
            sumFloat+=1
    return {list : sumList, int : sumInt, float : sumFloat, str : sumString, tuple : sumTuple}