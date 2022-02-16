
from tkinter import dialog
from turtle import color
from wordle_bot.game.runner import check, round, complete
import curses
import colorama
import time
from wordle_bot.game.display import displayGrid

#statistics:
#word -> any character shenanigans
#how many tries
#did it fail
#did it error
#wordle pattern

def run():

    colorama.init()
    #screen = curses.initscr()

    wordList = "../wordle-bot/wordle_bot/resources/guessOfficial.txt" #THE LIST OF WORDS IN THE WORDLE DICTIONARY, MUST CONTAIN ALL ANSWERS 
    answerList = "../wordle-bot/wordle_bot/resources/answerOfficial.txt" #THE LIST OF ANSWERS YOU PROVIDE. wordList MUST CONTAIN ALL OF THESE STRINGS

    with open(wordList, newline='') as f: #loads the word list
        loaded_words = list(f)

    with open(answerList, newline='') as f: #loads the answers
        loaded_answers = list(f)

    words = []


    for word in loaded_words: #removes trailing whitespace
        words.append(word.strip())
        
    saved = words
    back = words

    answers = []

    for word in loaded_answers:
        answers.append(word.strip())
        
    totalTurns = 0
    totalWords = 0
    totalErrors = 0
    totalFails = 0

    statsList = []
    
    correctWords = []
    turnListing = []
    
    paragraph = 14
    
    for word in answers:
        #turns 
        #correct
        #guesses
        #no. of possibilities
        #diagram
        #end distribution
        #average
        # % of list done
        
        #errors
        #failure?
        
        
        
        words = saved
        statsList.append(complete(words, word))
        #statsList[len(statsList - 1)](0)
        totalFails += statsList[len(statsList) - 1][5]
        
        turns = str(statsList[len(statsList) - 1][0])
        newWords = str(statsList[len(statsList) - 1][1])
        guessList = str(statsList[len(statsList) - 1][2])
        pLeft = str(statsList[len(statsList) - 1][3])
        diagram = statsList[len(statsList) - 1][4]
        distribution = [0,0,0,0,0,0]
        fails = totalFails
            
        for i in range(0, paragraph): #equal to # of printed lines
            print("                                                                                 ")        
        for i in range(0, paragraph): #equal to # of printed lines
            print("\033[A", end="")

        totalTurns += int(turns)
        totalWords += 1
        avg = str(totalTurns / totalWords)
        
        print("turns: " + turns)
        print("word: " + newWords)
        print("guesses: " + guessList)
        print("avg: " + avg)
        print("dictionary: " + pLeft)        
        for i in range(0, 6):
            if(i < len(diagram)):
                
                print(displayGrid(diagram[i]))
            else:
                print(" ")
        for i in statsList:
            distribution[i[0] - 1] += 1
            
        print("distribution: " + str(distribution))
        print("fails: " + str(fails))
        
        print(str(len(statsList)) + " / " + str(len(answers)))

        for i in range(0, paragraph): #equal to # of printed lines
            print("\033[A", end="")
        
        time.sleep(0.005)
        
        #screen.clear()
        
        #screen.addstr(1, 0, "turns: " + turns)
        #screen.addstr(2, 0, "word: " + newWords)
        #screen.addstr(3, 0, "guesses:" + guessList)
        #screen.addstr(4, 0, "avg: " + avg)
        #screen.addstr(5, 0, "words left: " + pLeft)
        
        #screen.addstr(12, 2, displayGrid("ggbgg"))
        #for i in range(6, 10):
        #    screen.addstr(i, 0, 'string: ' + str(i))
             
        #for i in range(0,5):
        #    screen.addstr(i + 11, 6, displayGrid(diagram[i]))
            
        #screen.refresh()

        #curses.napms(5000)
        

        #words = out[0]
        #turns = out[1]
        #correctWords.append(words)
        #turnListing.append(words)
        
        #totalWords += 1
        #totalTurns += turns
        #totalErrors += out[2]
        #totalFails += out[3]
    for i in range(0, paragraph): #equal to # of printed lines
            print("")
    #print(statsList[0][0])
    #avg = totalTurns / totalWords

    #print("words: " + str(totalWords))
    #print("turns: " + str(totalTurns))
    #print("avg: " + str(avg))
    #print("errors: " + str(totalErrors))
    #print("avg error: " + str(totalErrors / totalWords))
    #print("fails: " + str(totalFails))
    #print("avg fails: " + str(totalFails / totalWords))

    #print("---------")
