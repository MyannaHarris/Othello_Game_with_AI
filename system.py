#!/usr/bin/python
# AI
# 
# Myanna Harris, Jasmine Jans, and Carol Joplin
# 3-10-17
#
# Othello
# System

import sys
import time
from threading import Thread

from board import Board
from a import A
from p import P

class System(object):

    #constructor for the game
    def __init__(self, config):
        # make start board
        self.board = Board(config)
        self.board.printBoard()

        # declare the game done bool
        self.gameDone = False

        # make column dictionary for numbers that the column letters correspond to
        self.colDict = {
            'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

    #starts the game off and decides which player is which color
    def startGame(self):
        print("")
        inColor = raw_input("P would you like to be black (B) or white (W)? ")
        print("")
        print("Press q to quit")
        print("")
        
        #sets the ai and player to their correct colors
        if inColor == "B" or inColor == "b":
            self.ai = A(2)
            self.pl = P(1)
            self.playerMoves()
        else:
            self.ai = A(1)
            self.pl = P(2)
            self.aiMoves()

    #method to call from our thread to use with the timer
    def ai_input(self, L, ai, board):
        temp = ai.getMove(board)
        for move in temp:
            L.append(move)
        
    #makes a move for the player
    def playerMoves(self):
        #checks if the game is over
        if self.board.isDone(self.pl.getColor()):
            print("P cannot move")
            if self.gameDone:
                self.board.printWinner()
                sys.exit()
            else:
                self.gameDone = True
                self.aiMoves()
        else:
            self.gameDone = False
            confirmation = "N"
            #checks the users confirmation
            while confirmation != "Y" and confirmation != "y":
                '''row = ""
                col = ""
                
                L = []
                x = 1

                #creates a new thread for getting user input
                thread = Thread(target = self.user_input, args = (L,))
                thread.start()

                print("")
                print("P please make a move:")
                print("Row: ")

                #runs a ten second timer for the user to make a row move
                done = False

                while not done:
                    time.sleep(1)
                    if L:
                        row = L[0]
                        thread.join()
                        done = True
                    if not done:
                        print ("\n" + str(x) + "sec \n")
                        x += 1
                        if x > 10:
                            print("\nPress enter")
                            thread.join()
                            if self.pl.getColor() == 1:
                                # Black
                                print("Black forfeits")
                                print("White Wins")
                            else:
                                # White
                                print("White forfeits")
                                print("Black Wins")
                            sys.exit()
                            break

                L = []

                #creates a new thread for getting user input
                thread = Thread(target = self.user_input, args = (L,))
                thread.start()

                print("")
                print("Column: ")

                #runs a ten second timer for the user to make a row move
                done = False

                while not done:
                    time.sleep(1)
                    if L:
                        col = L[0]
                        thread.join()
                        done = True
                    if not done:
                        print ("\n" + str(x) + "sec \n")
                        x += 1
                        if x > 10:
                            print("\nPress enter")
                            thread.join()
                            if self.pl.getColor() == 1:
                                # Black
                                print("Black forfeits")
                                print("White Wins")
                            else:
                                # White
                                print("White forfeits")
                                print("Black Wins")
                            sys.exit()
                            break
                        '''
                
                # get move
                print("")
                print("P please make a move:")
                row = raw_input("Row: ")
                if row == "q":
                    sys.exit()
                col = raw_input("Column: ")
                if col == "q":
                    sys.exit()
                print("")

                #checks for validity of input
                if row.isdigit() and self.colDict.has_key(col):

                    # get indices
                    row = int(row) - 1
                    col = self.colDict[col]

                    #checks move legality
                    if self.board.isLegal(row, col, self.pl.getColor()):

                        if self.pl.getColor() == 1:
                            # Black
                            self.board.checkBlackMove(row, col)
                        else:
                            # White
                            self.board.checkWhiteMove(row, col)

                        print("")
                        #seeks confirmation from the AI
                        confirmation = raw_input("Is this correct A? (Y/N)")
                        if confirmation == "q":
                            sys.exit()
                        print("")

                        if confirmation == "Y" or confirmation == "y":
                            if self.pl.getColor() == 1:
                                # Black
                                self.board.blackMove(row, col)
                            else:
                                # White
                                self.board.whiteMove(row, col)

                            self.board.printBoard()
                    else:
                        print("")
                        print("Illegal move")
                        print("")
                else:
                    print("")
                    print("Illegal Input")
                    print("")

            self.aiMoves()

    #makes the moves for the ai (currently just another user)
    def aiMoves(self):
        print("")
        
        #seeks confirmaiton from P
        play = raw_input("A is about to play. P is this okay?(Y/N)")
        if play == "q" or play == "N" or play == "n":
            sys.exit()

        #checks if the game is over
        if self.board.isDone(self.ai.getColor()):
            print("A cannot move")
            if self.gameDone:
                self.board.printWinner()
                sys.exit()
            else:
                self.gameDone = True
                self.playerMoves()
        else:
            self.gameDone = False
            confirmation = "N"

            while confirmation != "Y" and confirmation != "y":
                row = ""
                col = ""
                
                L = []
                x = 1
                
                #creates a thread for getting the user input for a
                #   move during a timer
                thread = Thread(
                    target = self.ai_input, args = (L,self.ai,self.board,))
                thread.start()

                print("")
                print("A please make a move:")

                #creates a ten second time to make a move
                done = False

                while not done:
                    time.sleep(1)
                    if L:
                        thread.join()
                        done = True
                    if not done:
                        print ("\n" + str(x) + "sec \n")
                        x += 1
                        if x > 10:
                            print("\nPress enter")
                            thread.join()
                            if self.ai.getColor() == 1:
                                # Black
                                print("Black forfeits")
                                print("White Wins")
                            else:
                                # White
                                print("White forfeits")
                                print("Black Wins")
                            sys.exit()
                            break

                print("Row: " + str(int(L[0]) + 1))
                print("Column: " + str(L[1]))
                print("")

                row = L[0]
                col = L[1]

                #verifies valid move input
                if row.isdigit() and self.colDict.has_key(col):
                
                    # get indices
                    row = int(row)
                    col = self.colDict[col]

                    #checks to see if the move is legal
                    if self.board.isLegal(row, col, self.ai.getColor()):

                        if self.ai.getColor() == 1:
                            # Black
                            self.board.checkBlackMove(row, col)
                        else:
                            # White
                            self.board.checkWhiteMove(row, col)

                        print("")
                        #looks for confirmation from player
                        confirmation = raw_input("Is this correct P? (Y/N)")
                        if confirmation == "q":
                            sys.exit()
                        print("")

                        if confirmation == "Y" or confirmation == "y":
                            if self.ai.getColor() == 1:
                                # Black
                                self.board.blackMove(row, col)
                            else:
                                # White
                                self.board.whiteMove(row, col)

                            self.board.printBoard()

                    else:
                        print("")
                        print("Illegal move")
                        print("")
                else:
                    print("")
                    print("Illegal Input")
                    print("")

            self.playerMoves()



            
