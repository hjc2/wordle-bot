
from distutils import core
from hashlib import new
from operator import le
from turtle import pos

def green(words, letter, position):
    
    newWords = []
    
    for word in words:
        if(word[position] == letter):
            newWords.append(word)

    return(newWords)

def yellow(words, letter, position):
    
    staged = []
    newWords = []
    
    for word in words:
        if(word[position] != letter):
            staged.append(word)
            
    for word in staged:
        if(word.find(letter) != -1):
            newWords.append(word)

    return(newWords)



def greySolo(words, letter, position):
    newWords = []

    for word in words:
        if(word[position] != letter):
            newWords.append(word)
    

    return(newWords)

def greyAll(words, letter, position):
    
    newWords = []
    for word in words:    
        if letter not in word:
            newWords.append(word)

    return(newWords)