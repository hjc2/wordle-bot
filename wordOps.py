
from distutils import core
from hashlib import new
from operator import le
from turtle import pos
from typing import overload

def green(words, letter, position): #green box case
    #purges all words without the letter in the position
    newWords = []
    
    for word in words:
        if(word[position] == letter): 
            newWords.append(word)

    return(newWords)

def yellow(words, letter, position): #yellow box case
    #purges all words with the letter in position, but then adds all words with the letter (not in that position)
    staged = []
    newWords = []
    
    for word in words:
        if(word[position] != letter):
            staged.append(word)
            
    for word in staged:
        if(word.find(letter) != -1):
            newWords.append(word)

    return(newWords)


def greySolo(words, letter, position): #grey box case
    #purges all words with the letter in the position
    newWords = []

    for word in words:
        if(word[position] != letter):
            newWords.append(word)
    

    return(newWords)

def greyAll(words, letter): #grey box case (complete)
    #purges all words containing the letter
    newWords = []
    for word in words:    
        if letter not in word:
            newWords.append(word)

    return(newWords)