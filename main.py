
from wordOps import *
from display import *
from game import *

#filename = "allowed.txt"
#filename = "test."
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

#print(correctWords)

#back = green(back, "a", 0)
#back = green(back, "r", 1)

#back = grey(back, "c", 0)
#back = grey(back, "n", 3)
#back = grey(back, "e", 4)
#back = grey(back, "t", 2)

#back = yellow(back, "o", 3)

print("---------")
#print(back)

#print(correctWords)