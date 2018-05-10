# AI
# 
# Myanna Harris, Jasmine Jans, and Carol Joplin (jjans@gonzaga.zagmail.edu submitter)
# 3-10-17
#
# Othello
# AI - class that represents the AI of the othello game

class A(object):

    def __init__(self, color):
        # color
        # 1 = black
        # 2 = white
        self.color = color

        # dictionary from column letter to number
        self.colDictLettertoNum = {
            'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

        # dictionary from column number to letter
        self.colDictNumtoLetter = {
            0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H'}

    # returns color of ai
    def getColor(self):
        return self.color

    # returns the best move from alpha-beta pruning
    def getMove(self, board):
        move = []
        currBoard = board.getBoard()
        graph = self.makeGraph(currBoard)
        bestMove = self.mini_max(graph, "start")
        
        move.append(bestMove[0])
        move.append(bestMove[1])
        return move

    # make the graph of move options
    def makeGraph(self, currBoard):
        graph = {}
        # a move will be "1A" 1 = row, A = col
        # a hueristic will be saved as []
        # graph will be { "1A" : ["3B"]
        #                 "3B" : [5]}

        # heuristic = ai's # of tokens on the board

        graph["start"] = []

        for row in range(0, 8):
            for col in range(0,8):
                if currBoard[8 * row + col] == "-":
                    if self.isLegal(row, col, self.color, currBoard):
                        colLetter = self.colDictNumtoLetter[col]
                        graph["start"].append(str(row) + colLetter)

                        newBoard = []
                        for x in currBoard:
                            newBoard.append(x)

                        self.addMove(newBoard, self.color, row, col)

                        nextColor = 1
                        if self.color == 1:
                            nextColor = 2
                        
                        graph[str(row) + colLetter] = self.makeSubgraph(
                            newBoard, nextColor)

                        if len(graph[str(row) + colLetter]) < 1:
                            graph[str(row) + colLetter] = [str(
                                self.getNumAI(newBoard, row, col))]

                        else:

                            for move in graph[str(row) + colLetter]:
                                rowSub = int(move[0])
                                colSub = self.colDictLettertoNum[move[1]]

                                newSubBoard = []
                                for x in newBoard:
                                    newSubBoard.append(x)

                                self.addMove(newSubBoard, nextColor, rowSub, colSub)

                                graph[move] = self.makeSubgraph(
                                    newSubBoard, self.color)

                                if len(graph[move]) < 1:
                                    graph[move] = [str(self.getNumAI(
                                        newSubBoard, rowSub, colSub))]

                                else:
                                    for subMove in graph[move]:
                                        rSub = int(subMove[0])
                                        cSub = self.colDictLettertoNum[subMove[1]]

                                        subSubBoard = []
                                        for x in newSubBoard:
                                            subSubBoard.append(x)

                                        self.addMove(
                                            subSubBoard, self.color, rSub, cSub)

                                        graph[subMove] = [str(
                                            self.getNumAI(subSubBoard, rSub, cSub))]
                        
        return graph

    # Make the second level of move options
    def makeSubgraph(self, board, nextColor):
        subGraph = []
        
        for row in range(0, 8):
            for col in range(0,8):
                if board[8 * row + col] == "-":
                    if self.isLegal(row, col, nextColor, board):
                        colLetter = self.colDictNumtoLetter[col]
                        subGraph.append(str(row) + colLetter)
        return subGraph

    # add move to board
    def addMove(self, board, currColor, row, col):
        token = "B"
        if currColor == 2:
            token = "W"

        # Set space on board
        board[8 * row + col] = token

        # Set flipped spaces on board
        self.checkUpLeft(board, row-1, col-1, token, token)
        self.checkRight(board, row, col+1, token, token)
        self.checkLeft(board, row, col-1, token, token)
        self.checkUp(board, row-1, col, token, token)
        self.checkBottom(board, row+1, col, token, token)
        self.checkUpRight(board, row-1, col+1, token, token)
        self.checkBottomRight(board, row+1, col+1, token, token)
        self.checkBottomLeft(board, row+1, col-1, token, token)

    # gets the item (b, w, -) at the given coordinates
    def getItem(self, row, col, board):
        if row < 0 or row > 7 or col < 0 or col > 7:
            return ""
        return board[8 * row + col]
    
    # checks the legality of given coordinates
    def isLegal(self, row, col, currColor, board):
        token = "B"
        if currColor == 2:
            token = "W"
        
        nextToken = "W"
        if currColor == 2:
            nextToken = "B"
            
        #checks to see that its adjacent to an opposite piece
        if self.getItem(row + 1, col - 1, board) == nextToken:
            #checks to see that another same color piece sandwiches
            if self.checkForNextColor(row+2, col-2, 1, -1, token, board):
                return True
        if self.getItem(row + 1, col + 1, board) == nextToken:
            if self.checkForNextColor(row+2, col+2, 1, 1, token, board):
                return True
        if self.getItem(row + 1, col, board) == nextToken:
            if self.checkForNextColor(row+2, col, 1, 0, token, board):
                return True
        if self.getItem(row, col + 1, board) == nextToken:
            if self.checkForNextColor(row, col+2, 0, 1, token, board):
                return True
        if self.getItem(row, col - 1, board) == nextToken:
            if self.checkForNextColor(row, col-2, 0, -1, token, board):
                return True
        if self.getItem(row - 1, col - 1, board) == nextToken:
            if self.checkForNextColor(row-2, col-2, -1, -1, token, board):
                return True
        if self.getItem(row - 1, col, board) == nextToken:
            if self.checkForNextColor(row-2, col, -1, 0, token, board):
                return True
        if self.getItem(row - 1, col + 1, board) == nextToken:
            if self.checkForNextColor(row-2, col+2, -1, 1, token, board):
                return True
                
        return False

    # recursively checks for a valid move by searching for the current color
    # to sandwhich the opposite color in a given direction (by incRow, incCol)
    def checkForNextColor(self, row, col, incRow, incCol, checkColor, board):
        if (row < 0 or row > 7 or col < 0 or col > 7
            or board[8 * row + col] == "-"):
            return False
        if checkColor == board[8 * row + col]:
            return True

        if self.checkForNextColor(
            row+incRow, col+incCol, incRow, incCol, checkColor, board):
            return True

        return False

    # returns the number of tokens ai has on this board
    def getNumAI(self, board, row, col):
        numAI = 0
        total = 0

        corner = 0.0

        if ((row == 0 and col == 0) or
            (row == 0 and col == 7) or
            (row == 7 and col == 7) or
            (row == 7 and col == 0)):
            corner = 0.75

        token = "B"
        if self.color == 2:
            token = "W"

        for item in board:
            total += 1
            if item == token:
                numAI += 1

        tokenRatio = float(numAI)/total

        if corner > tokenRatio:
            return corner
        return tokenRatio

    # mini max with best first search
    def mini_max(self, G, start):
        visited = []
        pQueue = [start]
        pQueueV = [0]
        player = False
        
        while pQueue: #returns true if list has items, false otherwise
            vertex = pQueue.pop(0) #remove the most recently added item
            pQueueV.pop(0)

            # For stopping at best path
            if len(G[vertex]) > 0 and self.isReal((G[vertex])[0]):
                visited.append(vertex)
                return visited[1]
            
            if vertex not in visited:
                visited.append(vertex)
                children = G[vertex]
                
                vals = []
                for child in children:
                    vals.append(
                        self.alpha_beta(
                            G, child, -float("inf"), float("inf"), player))


                tempQ = []
                tempQVals = []
                for i in range(0, len(vals)):
                    currV = vals[i]

                    if len(tempQ) < 1:
                        tempQ.append(children[i])
                        tempQVals.append(currV)
                    else:
                        # Order temp list based on min or max
                        if not player:
                            for x in range(0, len(tempQ)):
                                if currV > tempQVals[x]:
                                    tempQ.insert(x, children[i])
                                    tempQVals.insert(x, currV)
                                    break
                                elif x == len(tempQ) - 1:
                                    tempQ.append(children[i])
                                    tempQVals.append(currV)
                        else:
                            for x in range(0, len(tempQ)):
                                if currV < tempQVals[x]:
                                    tempQ.insert(x, children[i])
                                    tempQVals.insert(x, currV)
                                    break
                                elif x == len(tempQ) - 1:
                                    tempQ.append(children[i])
                                    tempQVals.append(currV)


                # Add ordered nodes to priority queue                                          
                pQueue = tempQ + pQueue
                pQueueV = tempQVals + pQueueV
                player = not player

    # Alpha-beta pruning
    # player =  True max
    #           False min
    def alpha_beta(self, G, node, a, b, player):
        if G[node] == [] or self.isReal((G[node])[0]):
            # Return value
            if len(G[node]) > 0:
                heuristic = [float(i) for i in G[node]]
                if player:
                    return max(heuristic)
                else:
                    return min(heuristic)
            else:
                return 0

        if player:
            # max
            v = -float("inf")
            for child in G[node]:
                v = max(v, self.alpha_beta(G, child, a, b, False))
                a = max(a, v)
                if b <= a:
                    break
            return v
        else:
            # min
            v = float("inf")
            for child in G[node]:
                v = min(v, self.alpha_beta(G, child, a, b, True))
                b = min(b, v)
                if b <= a:
                    break
            return v

    # checks if string is a real number
    def isReal(self, txt):
        try:
            float(txt)
            return True
        except ValueError:
            return False

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
