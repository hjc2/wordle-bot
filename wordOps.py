
from distutils import core
from hashlib import new
from operator import le


def helloWorld():
    print("hello world")

def green(words, letter, position):
    
    newWords = []
    
    for word in words:
        if(word[position] == letter):
            newWords.append(word)

    tup = (newWords, letter, position)
    
    return(tup)

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



def grey(words, letter, correct, position):
    newWords = []

    for word in words:
            if(word.find(letter) == -1):
                newWords.append(word)
    
    return(newWords)

