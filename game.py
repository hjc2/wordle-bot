
from hashlib import new
from operator import le
from re import L
from display import check, displayGrid
from wordOps import *



def round(words, guess, correct):
    
    output = check(guess, correct)
        
    newWords = words
    
    for letter in range(0,5):
        if(output[letter] == "g"):
            newWords = green(newWords, guess[letter], letter)
        elif(output[letter] == "y"):
            newWords = yellow(newWords, guess[letter], letter)
        elif(output[letter] == "b"):
            newWords = grey(newWords, guess[letter], letter)
            
    return(newWords)

def run(words, correct):
    
    turns = 0
    
    startWord = "adieu"
    
    newWords = words
    
    guess = startWord
    
    while(len(newWords) > 1):
        
        newWords = round(newWords, guess, correct)
        #print(displayGrid(check(guess, correct)))
        guess = newWords[0]
        turns += 1

    statistics = (newWords, turns)
    return(statistics)
        
    