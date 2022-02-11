
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

def displayGrid(grid):
    board = ""
    
    for letter in range(0, 5):
        if(grid[letter] == "g"):
            board += "🟩"
        elif(grid[letter] == "b"):
            board += "⬛"    
        elif(grid[letter] == "y"):
            board += "🟨"
        
    return(board)