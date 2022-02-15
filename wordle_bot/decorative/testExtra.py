from wordle_bot.display import *
from wordle_bot.game.app import *

out = check("crane", "abbey")
print(out)

print(displayGrid(out))

a = "alpha"
b = "a"
print(a.count("a"))