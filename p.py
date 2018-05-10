# AI
# 
# Myanna Harris, Jasmine Jans, and Carol Joplin (jjans@gonzaga.zagmail.edu submitter)
# 3-10-17
#
# Othello
# Player - the class that represents a user player of the othello game

class P(object):

    def __init__(self, color):
        # color
        # 1 = black
        # 2 = white
        self.color = color

    def getColor(self):
        return self.color
