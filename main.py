
from wordOps import *

#filename = "allowed.txt"
filename = "test.txt"
#filename = "wordleV2.txt"

with open(filename, newline='') as f:
    loaded_words = list(f)

words = []
correctLetter = []
correctIndex = []

for word in loaded_words:
    words.append(word.strip())

tmp = green(words, "e", 4)
words = tmp[0]
correctLetter.append(tmp[1])
correctIndex.append(tmp[2])

words = grey(words, "3", 2)



print(words)



#if __name__ == "__main__":
#    main()