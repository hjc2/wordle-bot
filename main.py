
from wordOps import *
from display import *
from game import *

wordList = "wordleV2.txt" #THE LIST OF WORDS IN THE WORDLE DICTIONARY, MUST CONTAIN ALL ANSWERS 
answerList = "answerList.txt" #THE LIST OF ANSWERS YOU PROVIDE. wordList MUST CONTAIN ALL OF THESE STRINGS

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

correctWords = []
turnListing = []

for word in answers:
    words = saved
    out = run(words, word)
    words = out[0]
    turns = out[1]
    correctWords.append(words)
    turnListing.append(words)
    totalWords += 1
    totalTurns += turns
    totalErrors += out[2]
    totalFails += out[3]

avg = totalTurns / totalWords

print("words: " + str(totalWords))
print("turns: " + str(totalTurns))
print("avg: " + str(avg))
print("errors: " + str(totalErrors))
print("avg error: " + str(totalErrors / totalWords))
print("fails: " + str(totalFails))
print("avg fails: " + str(totalFails / totalWords))

print("---------")
