
from wordOps import *
from display import *
from game import *

#filename = "allowed.txt"
#filename = "test.txt"
filename = "wordleV2.txt"
answername = "answerList.txt"

with open(filename, newline='') as f:
    loaded_words = list(f)

with open(answername, newline='') as f:
    loaded_answers = list(f)

words = []

for word in loaded_words:
    words.append(word.strip())
saved = words
answers = []

for word in loaded_answers:
    answers.append(word.strip())
    

totalTurns = 0
totalWords = 0

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

avg = totalTurns / totalWords

print("words: " + str(totalWords))
print("turns: " + str(totalTurns))
print("avg: " + str(avg))
#print(correctWords)