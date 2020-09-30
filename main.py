#THIS IS THE MAIN FILE FOR CHESS PROJECT

################# IMPORTS GO HERE ######################
import pawn
import king
import queen
import bishop
import knight
import rook
########################################################


# True  -> White Piece Players Turn
# False -> Black Piece Players TUrn

currentPlayer = False   #Initially set to "False" will turn to "True" when the program execution starts.




# The main chess board
# The common notation for a piece would be "<color><piece>" example "wq" mean "<white><queen>"

board = [
    ["  1  ", "wr", "wk", "wb", "wk", "wq", "wb", "wk", "wr"],
    ["  2  ", "wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
    ["  3  ", "xx", "xx", "xx", "xx", "xx", "xx", "xx", "xx"],
    ["  4  ", "xx", "xx", "xx", "xx", "xx", "xx", "xx", "xx"],
    ["  5  ", "xx", "xx", "xx", "xx", "xx", "xx", "xx", "xx"],
    ["  6  ", "xx", "xx", "xx", "xx", "xx", "xx", "xx", "xx"],
    ["  7  ", "bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
    ["  8  ", "br", "bk", "bb", "bk", "bq", "bb", "bk", "br"],
    [" "],
    ["     ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 "],
]

# Note that board[0][0] is " 1 " not "wr". So if the input coordinates are x y it should be board[x-1][y]
# Try some examples to understand this.



# Function to check if the user entered piece is valid or not

def checkValidPos(x, y, cur):
    #print(x, y, cur)
    color = ""
    if cur == True:
        color = "w"
    else:
        color = "b"
    #print(board[x - 1][y][0], color)
    if x > 0 and x <= 8 and y > 0 and y <= 8:
        if board[x - 1][y][0] == color:           #if the piece is valid then should print valid moves and ask to input from that
            
            # SHOULD PRINT ALL THE VALID MOVES FIRST
            
            nx, ny = map(int, input().split())
            return True
        else:
            return False
    else:
        return False


# Function to get the coordinate of the piece that the user wants to move

def takeInput(cur): 
    x, y = map(int, input().split())
    if checkValidPos(x, y, cur):                    #checking if the user choose the correct piece i,e., Black player shouldnt choose white piece or any user shouldnt chooose empty position
        return True
    else:
        print("error enter again")
        takeInput(cur)



# Main driver Function

def main():
    global currentPlayer                            # To make changes of global variable in local scope we have to use "global" keyword
    while True:
        currentPlayer = not currentPlayer           # Changing the color of the currentplayer to next player
        for i in board:     
            print(*i, sep="  ")                     # Printing the board.
        value = takeInput(currentPlayer)            # Taking input from the user passing currentPlayer as the parameter
        if value == True:                           # At the end of one successfull iteration it should return True 
            main()

main() #calling main function for the first time

