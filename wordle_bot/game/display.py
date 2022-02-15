
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