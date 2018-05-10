# AI
# 
# Myanna Harris, Jasmine Jans, and Carol Joplin (jjans@gonzaga.zagmail.edu submitter)
# 3-10-17
#
# Othello
# Board: Class that represents the board used in the game of othello.
#        Board is 8x8 with letters across the columns and numbers down the rows.
#

class Board(object):

    # constructor to set up board with first 4 tokens based
    # on the config parameter
    def __init__(self, config):

        # set up scores
        self.black = 2
        self.white = 2

        # set up empty board
        # array
        # row = 0, 8, 16, ... = 8 * row
        # column = 0, 1, 2, 3, ... = col
        # position in grid = 8 * row + col
        self.board = ["-" for x in range(0, 64)]
        
        # center of board is 3,3 3,4 4,3 4,4
        if config == 1:
            # WB
            # BW
            self.board[8 * 3 + 3] = 'W'
            self.board[8 * 3 + 4] = 'B'
            self.board[8 * 4 + 3] = 'B'
            self.board[8 * 4 + 4] = 'W'
        else:
            # BW
            # WB
            self.board[8 * 3 + 3] = 'B'
            self.board[8 * 3 + 4] = 'W'
            self.board[8 * 4 + 3] = 'W'
            self.board[8 * 4 + 4] = 'B'

    # Returns a copy of the board array
    def getBoard(self):
        copyBoard = []
        for x in self.board:
            copyBoard.append(x)
        return copyBoard

    # displays board, aka prints out the current score and
    # current board configuration
    def printBoard(self):
        # Print score
        print("")
        print("White: " + str(self.white))
        print("Black: " + str(self.black))
        print("")
        
        # Print board 
        print("  A B C D E F G H")
        for row in range(0, 8):
            printStr = str(row + 1)
            for col in range(0, 8):
                printStr += " " + self.board[8 * row + col]

            print(printStr)
        print("")

    # display checking board, aka board that checks the move
    # wanting to be places
    def printCheckBoard(self, checkBoard):
        # Print board 
        print("  A B C D E F G H")
        for row in range(0, 8):
            printStr = str(row + 1)
            for col in range(0, 8):
                printStr += " " + checkBoard[8 * row + col]

            print(printStr)

    # Checks the next black move to see if it is legal and
    # creates a new "check board" to be printed to verify the move
    def checkBlackMove(self, row, col):
        copy = self.board[:]
        copy[8 * row + col] = 'B'

        #check all of the surrounding squares of the move
        self.checkUpLeft(copy, row-1, col-1, "B", "X")
        self.checkRight(copy, row, col+1, "B", "X")
        self.checkLeft(copy, row, col-1, "B", "X")
        self.checkUp(copy, row-1, col, "B", "X")
        self.checkBottom(copy, row+1, col, "B", "X")
        self.checkUpRight(copy, row-1, col+1, "B", "X")
        self.checkBottomRight(copy, row+1, col+1, "B", "X")
        self.checkBottomLeft(copy, row+1, col-1, "B", "X")

        #print out the checking board
        self.printCheckBoard(copy)

    # Checks the next white move to see if it is legal and
    # creates a new "check board" to be printed to verify the move
    def checkWhiteMove(self, row, col):
        copy = self.board[:]
        copy[8 * row + col] = 'W'

        #check all of the surrounding squares of the move
        self.checkUpLeft(copy, row-1, col-1, "W", "X")
        self.checkRight(copy, row, col+1, "W", "X")
        self.checkLeft(copy, row, col-1, "W", "X")
        self.checkUp(copy, row-1, col, "W", "X")
        self.checkBottom(copy, row+1, col, "W", "X")
        self.checkUpRight(copy, row-1, col+1, "W", "X")
        self.checkBottomRight(copy, row+1, col+1, "W", "X")
        self.checkBottomLeft(copy, row+1, col-1, "W", "X")

        #print out the checking board
        self.printCheckBoard(copy)

    #the following 8 "check" methods check in all the directions for certain
    #pieces that will flip colors if a given move is made. It then
    #replaces those pieces with the given newItem

    # check upLeft items
    def checkUpLeft(self, currBoard, row, col, currColor, newItem):
        if (row < 0 or row > 7 or col < 0 or col > 7 or
            currBoard[8 * row + col] == "-"):
            return False
        if currColor == currBoard[8 * row + col]:
            return True

        if self.checkUpLeft(currBoard, row-1, col-1, currColor, newItem):
            currBoard[8 * row + col] = newItem
            return True

        return False

    # check upRight items
    def checkUpRight(self, currBoard, row, col, currColor, newItem):
        if (row < 0 or row > 7 or col < 0 or col > 7 or
            currBoard[8 * row + col] == "-"):
            return False
        if currColor == currBoard[8 * row + col]:
            return True

        if self.checkUpRight(currBoard, row-1, col+1, currColor, newItem):
            currBoard[8 * row + col] = newItem
            return True
        
        return False
        
    # check bottomLeft items
    def checkBottomLeft(self, currBoard, row, col, currColor, newItem):
        if (row < 0 or row > 7 or col < 0 or col > 7 or
            currBoard[8 * row + col] == "-"):
            return False
        if currColor == currBoard[8 * row + col]:
            return True

        if self.checkBottomLeft(currBoard, row+1, col-1, currColor, newItem):
            currBoard[8 * row + col] = newItem
            return True

        return False

    # check BottomRight items
    def checkBottomRight(self, currBoard, row, col, currColor, newItem):
        if (row < 0 or row > 7 or col < 0 or col > 7 or
            currBoard[8 * row + col] == "-"):
            return False
        if currColor == currBoard[8 * row + col]:
            return True

        if self.checkBottomRight(currBoard, row+1, col+1, currColor, newItem):
            currBoard[8 * row + col] = newItem
            return True

        return False

    # check up items
    def checkUp(self, currBoard, row, col, currColor, newItem):
        if (row < 0 or row > 7 or col < 0 or col > 7 or
            currBoard[8 * row + col] == "-"):
            return False
        if currColor == currBoard[8 * row + col]:
            return True

        if self.checkUp(currBoard, row-1, col, currColor, newItem):
            currBoard[8 * row + col] = newItem
            return True
        
        return False

    # check right items
    def checkRight(self, currBoard, row, col, currColor, newItem):
        if (row < 0 or row > 7 or col < 0 or col > 7 or
            currBoard[8 * row + col] == "-"):
            return False
        if currColor == currBoard[8 * row + col]:
            return True

        if self.checkRight(currBoard, row, col+1, currColor, newItem):
            currBoard[8 * row + col] = newItem
            return True

        return False

    # check left items
    def checkLeft(self, currBoard, row, col, currColor, newItem):
        if (row < 0 or row > 7 or col < 0 or col > 7 or
            currBoard[8 * row + col] == "-"):
            return False
        if currColor == currBoard[8 * row + col]:
            return True

        if self.checkLeft(currBoard, row, col-1, currColor, newItem):
            currBoard[8 * row + col] = newItem
            return True

        return False

    # check bottom items
    def checkBottom(self, currBoard, row, col, currColor, newItem):
        if (row < 0 or row > 7 or col < 0 or col > 7 or
            currBoard[8 * row + col] == "-"):
            return False
        if currColor == currBoard[8 * row + col]:
            return True

        if self.checkBottom(currBoard, row+1, col, currColor, newItem):
            currBoard[8 * row + col] = newItem
            return True

        return False

    # Add black move, make the new move on the actual board
    # and update the score
    def blackMove(self, row, col):
        self.board[8 * row + col] = 'B'

        self.checkUpLeft(self.board, row-1, col-1, "B", "B")
        self.checkRight(self.board, row, col+1, "B", "B")
        self.checkLeft(self.board, row, col-1, "B", "B")
        self.checkUp(self.board, row-1, col, "B", "B")
        self.checkBottom(self.board, row+1, col, "B", "B")
        self.checkUpRight(self.board, row-1, col+1, "B", "B")
        self.checkBottomRight(self.board, row+1, col+1, "B", "B")
        self.checkBottomLeft(self.board, row+1, col-1, "B", "B")

        self.setScore()

    # Add white move, make the new move on the actual board
    # and update the score
    def whiteMove(self, row, col):
        self.board[8 * row + col] = 'W'

        self.checkUpLeft(self.board, row-1, col-1, "W", "W")
        self.checkRight(self.board, row, col+1, "W", "W")
        self.checkLeft(self.board, row, col-1, "W", "W")
        self.checkUp(self.board, row-1, col, "W", "W")
        self.checkBottom(self.board, row+1, col, "W", "W")
        self.checkUpRight(self.board, row-1, col+1, "W", "W")
        self.checkBottomRight(self.board, row+1, col+1, "W", "W")
        self.checkBottomLeft(self.board, row+1, col-1, "W", "W")

        self.setScore()

    # checks if game is done, aka if there are no legal moves left
    def isDone(self, color):
        for i in range(0, 8):
            for j in range(0, 8):
                if self.board[8 * i + j] == "-":
                    if self.isLegal(i, j, color):
                        return False
        return True

    # gets the item (b, w, -) at the given coordinates
    def getItem(self, row, col):
        if row < 0 or row > 7 or col < 0 or col > 7:
            return ""
        return self.board[8 * row + col]

    # checks the legality of given coordinates
    def isLegal(self, row, col, currColor):
        # get current color and opposing color
        token = "B"
        if currColor == 2:
            token = "W"
        
        nextToken = "W"
        if currColor == 2:
            nextToken = "B"
        
        #checks to see that its adjacent to an opposite piece
        if self.getItem(row + 1, col - 1) == nextToken:
            #checks to see that another same color piece sandwiches
            if self.checkForNextColor(row+2, col-2, 1, -1, token):
                return True
        if self.getItem(row + 1, col + 1) == nextToken:
            if self.checkForNextColor(row+2, col+2, 1, 1, token):
                return True
        if self.getItem(row + 1, col) == nextToken:
            if self.checkForNextColor(row+2, col, 1, 0, token):
                return True
        if self.getItem(row, col + 1) == nextToken:
            if self.checkForNextColor(row, col+2, 0, 1, token):
                return True
        if self.getItem(row, col - 1) == nextToken:
            if self.checkForNextColor(row, col-2, 0, -1, token):
                return True
        if self.getItem(row - 1, col - 1) == nextToken:
            if self.checkForNextColor(row-2, col-2, -1, -1, token):
                return True
        if self.getItem(row - 1, col) == nextToken:
            if self.checkForNextColor(row-2, col, -1, 0, token):
                return True
        if self.getItem(row - 1, col + 1) == nextToken:
            if self.checkForNextColor(row-2, col+2, -1, 1, token):
                return True
                
        return False

    # recursively checks for a valid move by searching for the current color
    # to sandwhich the opposite color in a given direction (by incRow, incCol)
    def checkForNextColor(self, row, col, incRow, incCol, checkColor):
        if (row < 0 or row > 7 or col < 0 or col > 7
            or self.board[8 * row + col] == "-"):
            return False
        if checkColor == self.board[8 * row + col]:
            return True

        if self.checkForNextColor(row+incRow, col+incCol, incRow, incCol, checkColor):
            return True

        return False

    # set new score for board, counts all the black and white pieces on the board
    def setScore(self):
        self.white = 0
        self.black = 0

        for item in self.board:
            if item == "B":
                self.black += 1
            elif item == "W":
                self.white += 1

    # prints the winner of the game
    def printWinner(self):
        if self.white > self.black:
            print("White wins")
        elif self.black > self.white:
            print("Black wins")
        else:
            print("Tie")
            
