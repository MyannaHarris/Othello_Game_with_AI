# AI
# 
# Myanna Harris, Jasmine Jans, and Carol Joplin (jjans@gonzaga.zagmail.edu submitter)
# 3-10-17
#
# Othello
#
# To run: python othello.py #
# # = 1 for WB start
# # = 2 for BW start

import sys
from system import System

def main(argv):
    #starts the game with the given configuration if given a command line param
    if (len(argv) > 0):
        system = System(int(argv[0]))
    
    #starts the game from the System class
    system.startGame()
        

if __name__ == '__main__':
    main(sys.argv[1:])
