
import curses

import sys
import os

screen = curses.initscr()

def displayMe(spell, info):
    spell.addstr(0, 0, str(info))
    spell.ref

for i in range(1, 100):    
    curses.napms(10)

    #print(str(i) + '\r\r\r\r\r\r\r\r', sep='', end ='', file = sys.stdout , flush = False)
    
    #sys.stdout.flush()
    #os.system('cls')