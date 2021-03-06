
from distutils.log import error

from numpy import diag
from pytest import fail
from wordle_bot.game.display import displayGrid
from wordle_bot.game.wordOps import green, yellow, greySolo, greyAll


with open('../output.output.txt') as f:
def check(guess, correct):
    
    redone = list(correct)
    grid = ""
    for letter in range(0, 5):
        if(guess[letter] == redone[letter]):
            grid = grid + "g"
            redone[letter] = "*"
        elif guess[letter] not in redone:
            grid = grid + "b"
        elif guess[letter] in redone:
            grid = grid + "y"
            redone[letter] = "*"              
            
    return(grid)

def round(words, guess, correct):
    
    output = check(guess, correct)
        
    newWords = words
    
    for letter in range(0,5):
        if(output[letter] == "g"): #green box case
            newWords = green(newWords, guess[letter], letter)
        elif(output[letter] == "y"): #yellow box case
            newWords = yellow(newWords, guess[letter], letter)
        elif(output[letter] == "b"): #grey box case
            if guess[letter] not in correct: #no repeats
                newWords = greyAll(newWords, guess[letter]) #purge all containing letter
            else:
                newWords = greySolo(newWords ,guess[letter], letter) #purge just this slot for this letter
    
    statistics = (newWords, output)

    return(statistics)

def complete(words, correct):
    turns = 0
    errors = 0
    fails = 0
    guessList = []
    pLeft = []
    diagram = []
    
    startWord = "adieu"
    
    newWords = words
    
    guess = startWord
    
    #print(correct)

    while(len(newWords) > 1):
        
        guessList.append(guess)
        pLeft.append(len(newWords))

        rounder = round(newWords, guess, correct)
        data = rounder[0]
        
        diagram.append(rounder[1])
        
        if(len(data) > 0):
            newWords = round(newWords, guess, correct)[0]
        else:
            guess = correct
            errors += 1
        #print(displayGrid(check(guess, correct)) + " " + str(guess))

        if(turns >= 5):
            guess = correct
            fails += 1
            newWords = [correct]
        if(guess == correct):
            newWords = [guess]
        else:
            
            if(len(newWords) >= 1):
                    #print("next")
                    guess = newWords[0]
                    #if(len(newWords) > 5):
                    #    guess = newWords[randint(0,3)]
            
            elif(len(newWords) == 0):
                #print("ERROR")
                errors += 1
            
            #print(guess + ": " + str(turns))
            
            turns += 1
                #print("next")
            #elif(len(newWords) == 0):
                #print("ERROR")
            #print(" ")
        
    #print("\n\n")
    statistics = (turns + 1, newWords, guessList, pLeft, diagram, fails)
    
    
    return(statistics)
        
    