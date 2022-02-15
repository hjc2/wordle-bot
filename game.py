
from hashlib import new
from operator import le
from random import randint
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
        #elif(output[letter] == "b"):
        #    newWords = greySolo(newWords, guess[letter], letter)  
        
        elif(output[letter] == "b"):  
            
            counted = 0
            for counter in range(0,5):
                if(guess[letter] == guess[counter]):
                    counted += 1
            if(counted > 1): #overlap case
                newWords = greySolo(newWords, guess[letter], letter)
            if guess[letter] not in correct:
                newWords = greyAll(newWords, guess[letter], letter)
            
            
        #elif(output[letter] == "b"):
        #    if(correct.count(guess[letter]) > 1):
        #        newWords = greySolo(newWords, guess[letter], letter)
        #    elif(output.count(guess) == 1):
        #        newWords = greyAll(newWords, guess[letter], letter)
            
    return(newWords)

def run(words, correct):
    turns = 0
    errors = 0
    fails = 0
    
    startWord = "crane"
    
    newWords = words
    
    guess = startWord
    
    print(correct)

    while(len(newWords) > 1):
        
        newWords = round(newWords, guess, correct)
        
        print(displayGrid(check(guess, correct)) + " " + str(guess))

        if(turns >= 6):
            guess = correct
            fails += 1
        if(guess == correct):
            newWords = [guess]
        else:
            
            if(len(newWords) >= 1):
                    #print("next")
                    guess = newWords[0]
                    #if(len(newWords) > 5):
                    #    guess = newWords[randint(0,3)]
            
            elif(len(newWords) == 0):
                print("ERROR")
                errors += 1
            
            #print(guess + ": " + str(turns))
            
            turns += 1
                #print("next")
            #elif(len(newWords) == 0):
                #print("ERROR")
            #print(" ")
        
    print("\n\n")
    statistics = (newWords, turns, errors, fails)
    return(statistics)
        
    