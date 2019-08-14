# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 15:59:04 2018

@author: spanier
"""
def replaceSimaneyPisuk(mahrozet):
    simaneyPisuk = ",.;:!?\t\n"
    newMahrozet = ""
    for c in mahrozet:
        if c in simaneyPisuk:
            newMahrozet += ' '
        else:
            newMahrozet += c
    return newMahrozet
#
def countWords(fileObj):
    D = dict([])
    for line in fileObj:
        wordsInLine = replaceSimaneyPisuk(line).split()
        for word in wordsInLine:
            if word not in D:
                D[word] = 1
            else:
                D[word] += 1
                return D
#
def prtWordCounts(D):
    prtLines = 1
    for word, count in D.items():
        if prtLines != 10:
            print(word, "was found", count, "times in the text.")
            prtLines += 1
        else:
            while True:
                ifBreak = input("Do you wish to stop printing? (Y, y, N or n)").upper()
                if ifBreak == 'Y':
                    print ('The printing of the word counts was stopped.')
                    return 
                elif ifBreak == 'N':
                    prtLines = 1
                    break
                #else:
                  #  continue
                else:
                    print ('All the word counts were printed')
                    return
#
#
# main program
#
if __name__ == "__main__":
    fileName = input("Please, enter the text file to be processed: ")
# in this program I use exception handling, but the students may
# write their program assuming that the text file exists
try:
    fileObj = open(fileName, "r")
    D = countWords(fileObj)
    prtWordCounts(D)
    fileObj.close()
except FileNotFoundError:
    print ("ERROR - file ", fileName, "not found!")
#