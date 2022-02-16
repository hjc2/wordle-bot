
from wordle_bot.game.runner import check, round, complete
import curses

#statistics:
#word -> any character shenanigans
#how many tries
#did it fail
#did it error
#wordle pattern

def run():

    screen = curses.initscr()

    wordList = "../wordle-bot/wordle_bot/resources/wordleV2.txt" #THE LIST OF WORDS IN THE WORDLE DICTIONARY, MUST CONTAIN ALL ANSWERS 
    answerList = "../wordle-bot/wordle_bot/resources/answerList.txt" #THE LIST OF ANSWERS YOU PROVIDE. wordList MUST CONTAIN ALL OF THESE STRINGS

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
        
        turns = str(statsList[len(statsList) - 1][0])
        newWords = str(statsList[len(statsList) - 1][1])
        guessList = str(statsList[len(statsList) - 1][2])

        totalTurns += int(turns)
        totalWords += 1
        avg = str(totalTurns / totalWords)
        
        screen.addstr(1, 0, turns)
        screen.addstr(2, 0, newWords)
        screen.addstr(3, 0, guessList)
        screen.addstr(4, 0, avg)

        
        screen.refresh()
        
        #words = out[0]
        #turns = out[1]
        #correctWords.append(words)
        #turnListing.append(words)
        
        #totalWords += 1
        #totalTurns += turns
        #totalErrors += out[2]
        #totalFails += out[3]
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
