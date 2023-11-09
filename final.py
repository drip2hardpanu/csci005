import random

class Board:
    """A data type representing a mancala board
    """

#a menu for the game
    def menu(self):
        """Prints the menu of options that the user can choose."""
        print()
        print("(0) Player vs Player")
        print("(1) Player vs Random AI")
        print("(2) Player vs AI lvl 1 (will attempt replay loops)")
        print("(3) Player vs AI lvl 2")
        print("(8) Show current Score")
        print("(9) Leave and Show Score")

        print()

#a scoreboard for the game




#representation and data
    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[4]*width for row in range(height+1)]

        ##Manual Changes

        #midboard
        self.data[1][0] = 0
        self.data[1][7] = 0
        
        #corners of board
        self.data[0][0] = 'X'
        self.data[0][7] = 'X'
        self.data[2][0] = 'X'
        self.data[2][7] = 'X'

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board, in this case a mancala board
        """

        s = ''   # the string to return
        s += (2*self.width+1) * ' '  + '\n'

        for row in range(0,1):
            s += ' '   
            for col in range(0,self.width):
                s += str(self.data[row][col]) + ' '
            s += '\n'
    
        s += '   ' + (2*self.width-5) * ' ' + '   '+ '\n' 
        s += ' ' + str(self.data[1][0]) + 6*'  ' + ' '+ str(self.data[1][7]) + " "
        s += "\n"
        s += '   ' + (2*self.width-5) * ' ' + '   '+'\n' 

        for row in range(1,2):
            s += ' '   
            for col in range(0,self.width):
                s += str(self.data[row+1][col]) + ' '
            s += '\n'

        s += (2*self.width+1) * ' ' + '\n' #bottom of the board


        #adding numbers
        for col in range(self.width):
            s += ' ' + str(col%10)

        return s       # the board is complete, return it


##Tools
#make move tool, needed to make moves
    def makeMove(self, side, col):
        """usage: makeMove(self, col, ox), col represents the index of the column to which the beads will be moved, makes the move and accounts for last bead capture rule"""
        newcol = col
        if side == 'B':
            row = 2
            newrow = row
            while self.data[row][col] != 0:
                self.data[row][col] -= 1
                if newcol == 6 and newrow == 0:
                    newcol -= 1
                    self.data[newrow][newcol] += 1
                
                elif newcol < 6 and newrow == 2:
                    newcol += 1
                    self.data[newrow][newcol] += 1
                elif newcol == 6 and newrow == 2:
                    newcol += 1
                    newrow = 0
                    self.data[1][newcol] += 1

                elif newcol == 1 and newrow == 0:
                    newrow = 2
                    self.data[newrow][newcol] += 1

                elif newcol < 7 and newrow == 0:
                    newcol -= 1
                    self.data[newrow][newcol] += 1

                elif newcol == 7 and newrow == 0:
                    newcol -= 1
                    self.data[newrow][newcol] += 1

                
                #empty hole on bottom rule
            if self.data[newrow][newcol] == 1 and newrow == 2:
                if newrow == 2:
                    newrow1 = 0
                
                if self.data[newrow1][newcol] > 0:
                    self.data[1][7] += self.data[newrow1][newcol] + 1 
                    self.data[newrow1][newcol] = 0
                    self.data[newrow][newcol] = 0

                #endgame rule
        if sum(b.data[2][1:7]) == 0:
            self.data[1][0] += sum(b.data[0][1:7])
            self.rowclear(0)

        elif side == 'T':
            row = 0
            newrow = row
            while self.data[row][col] != 0:
                self.data[row][col] -= 1
                if newcol == 0 and newrow == 2:
                    newcol += 1
                    self.data[newrow][newcol] += 1
                
                elif newcol < 6 and newrow == 2:
                    newcol += 1
                    self.data[newrow][newcol] += 1
                elif newcol == 6 and newrow == 2:
                    newrow = 0
                    self.data[newrow][newcol] += 1

                
                ##top

                elif newcol == 1 and newrow == 0:
                    newcol = 0
                    newrow = 2
                    self.data[1][0] += 1

                elif newcol < 7 and newrow == 0:
                    newcol -= 1
                    self.data[newrow][newcol] += 1
                
                elif newcol == 7 and newrow == 0:
                    newcol -= 1
                    self.data[newrow][newcol] += 1

                #empty hole on top rule
            if self.data[newrow][newcol] == 1 and newrow == 0:
                if newrow == 0:
                    newrow1 = 2
                
                if self.data[newrow1][newcol] > 0:
                    self.data[1][0] += self.data[newrow1][newcol] + 1 
                    self.data[newrow1][newcol] = 0
                    self.data[newrow][newcol] = 0

            #endgame rule
        if sum(b.data[0][1:7]) == 0:
            self.data[1][7] += sum(b.data[2][1:7])
            self.rowclear(2)

#copy tools, beneficial in lvl 2 ai
    def OneCopy(self):
        '''This will copy b one time, which will be useful for one move ahead AI 
        output -- b2''' 
        height = 2
        width = 8

        for row in range(height):
            for col in range(width):
                # b copied to b2
                b2.data[row][col] = self.data[row][col]
        
    def OneCopyReverse(self):
        '''This is used similar to a paste function, allows you to take stored data of a board and push it onto default board''' 
        height = 2
        width = 8

        for row in range(height):
            for col in range(width):
                # b copied to b2
                self.data[row][col] = b2.data[row][col]

#clear/reset tools
    def clear(self):
        "This will clear the board"
        for row in range(self.height + 1):
            for col in range(1,7):
                self.data[row][col] = 0
    
    def rowclear(self,row):
        "This will clear a specified row int he board"
        for col in range(1,7):
            self.data[row][col] = 0

    def reset(self):
        '''resets the board to its default configuration'''
        self.data[1][0] = 0
        self.data[1][7] = 0

        for col in range(1,7):
            self.data[0][col] = 4
        
        for col in range(1,7):
            self.data[2][col] = 4

### see if the move is allowed:
    def checkIfIntable(self, inp):
        '''acc of allows move, checks to see if an input is intable'''
        try:
            column1 = int(inp)
            return True
        except:
            return False
        
    def allowsMove(self, side, col):
        """usage: allowMoves(self, c), checks to see if a move is allowed
        checks bounds, integer input, and pot"""
        if side == 'T':
            row = 0
        elif side == 'B':
            row = 2
        else:
            return False
        
        if self.checkIfIntable(col) == False:
            return False
        elif int(col) < 1:
            return False
        elif int(col) > 6:
            return False
        elif self.data[row][int(col)] == 0:
            return False
        else:
            return True
        
    ##end game
    def checkEmpty(self):
        "checks if the board (not including point pots) is empty"
        if sum(self.data[0][1:7]) + sum(self.data[2][1:7]) == 0:
            return True
        else:
            return False
    
    def CheckEmptyRowTOP(self):
        '''UNUSED: Checks to see if the top row is empty'''
        if sum(self.data[0][1:7]) == 0:
            return True
        else:
            return False
        
    def CheckEmptyRowBOT(self):
        '''UNUSED: checks to see if the bottom row is empty'''
        if sum(self.data[2][1:7]) == 0:
            return True
        else:
            return False

    def checkWin(self):
        "checks to see who won on an empty board"
        if self.data[1][0] > self.data[1][7]:
            winner = 'T'
            print('top wins!')
        elif self.data[1][0] < self.data[1][7]:
            winner = 'B'
            print('bottom wins!')
        else:
            winner = 'neither'
            print('tie')
        
        return winner


##bead replay checks + loops

    #bead replay check for the top
    def checkLastBeadReplayTop(self, col):
        "checks if the last bead rule applied for TOP"
        row = 0
        
        if col == 1:
            if self.data[row][col] == 1:
                return True
            elif (self.data[row][col]) % 13 == 1:
                return True
            else:
                return False
        elif col == 2:
            if self.data[row][col] == 2:
                return True
            elif (self.data[row][col]) % 13 == 2:
                return True
            else:
                return False
        elif col == 3:
            if self.data[row][col] == 3:
                return True
            elif (self.data[row][col]) % 13 == 3:
                return True
            else:
                return False
        elif col == 4:
            if self.data[row][col] == 4:
                return True
            elif (self.data[row][col]) % 13 == 4:
                return True
            else:
                return False
        elif col == 5:
            if self.data[row][col] == 5:
                return True
            elif (self.data[row][col]) % 13 == 5:
                return True
            else:
                return False
        elif col == 6:
            if self.data[row][col] == 6:
                return True
            elif (self.data[row][col]) % 13 == 6:
                return True
            else:
                return False
        else:
            return False
        
    #bead replay lopp for top
    def beadReplayLoopTOP(self, col):
        '''bead replay loop for the top, ensures there is no capacity on where the replay loop stops'''
        while self.checkLastBeadReplayTop(col) == True:
            self.makeMove('T', col)

            if self.checkEmpty() == True:
                break

            print("last bead rule")
            print(b)


            newcol = int(input("what column would you (top) like to pick? "))

            if self.allowsMove('T', newcol) == False:
                newcol = 0
                while self.allowsMove('T', newcol) == False:
                    print("that doesn't work")
                    newcol = int(input("choose another "))
           
            col = newcol
            
            if self.checkLastBeadReplayTop(col) == False:
                self.makeMove('T', newcol)

    #bead replay check for bottom 
    def checkLastBeadReplayBottom(self, col):
        "checks if the last bead rule applies (bottom)"
        row = 2
        
        if col == 1:
            if self.data[row][col]  == 6:
                return True
            elif (self.data[row][col] ) % 13 == 6:
                return True
            else:
                return False
        elif col == 2:
            if self.data[row][col]  == 5:
                return True
            elif (self.data[row][col]) % 13 == 5:
                return True
            else:
                return False
        elif col == 3:
            if self.data[row][col]  == 4:
                return True
            elif self.data[row][col] % 13 == 4:
                return True
            else:
                return False
        elif col == 4:
            if self.data[row][col]  == 3:
                return True
            elif self.data[row][col] % 13 == 3:
                return True
            else:
                return False
        elif col == 5:
            if self.data[row][col] == 2:
                return True
            elif (self.data[row][col]) % 13 == 2:
                return True
            else:
                return False
        elif col == 6:
            if self.data[row][col] == 1:
                return True
            elif (self.data[row][col]) % 13 == 1:
                return True
            else:
                return False
        else:
            return False

    #bead replay loop for bottom
    def beadReplayLoopBot(self, col):
        '''Bead replay loop for the bottom (i.e., the player), ensures the amount of replays isn't limited'''
        while self.checkLastBeadReplayBottom(col) == True:
            #make the move you came in with
            self.makeMove('B', col)

            if self.checkEmpty() == True:
                break

            #print the last bead rule and the board
            print("last bead rule")
            print(b)

            #take in the newcol
            newcol = int(input("what column would you (bottom) like to pick? "))

            #check if the move is allowed
            if self.allowsMove('B', newcol) == False:
                newcol = 0
                while self.allowsMove('B', newcol) == False:
                    print("that doesn't work")
                    newcol = int(input("choose another"))


            #set the new variable accordingly
            col = newcol

            #check for last bead rule
            if self.checkLastBeadReplayBottom(col) == False:
                self.makeMove('B', newcol)

#AI
        
    ##Random AI
    def randomAI(self):
        "Random AI, pretty self explanatory, plays randomly"
        col = int(random.choice(range(1,7)))
        
        if self.allowsMove('T', col) == False:
                col = 0
                while self.allowsMove('T', col) == False:
                    col = int(random.choice(range(1,7)))

        print("I chose " + str(col))

        if self.checkLastBeadReplayTop(col) == True:
            self.beadReplayLoopRDMai(col)
        else:
            self.makeMove('T', col)

    ##RandomAI beadReplayLoop
    def beadReplayLoopRDMai(self, col):
        '''bead replay loop for the ai, this is used to ensure that the AI can run as many replays as available'''
        #while loop for multiple iterations
        while self.checkLastBeadReplayTop(col) == True:
            self.makeMove('T', col)

            #checks if the board is empty
            if self.checkEmpty():
                break

            print("last bead rule")
            print(b)

            #input
            col = random.choice(range(1,7))
                     
            if self.allowsMove('T', col) == False:
                col = 0
                while self.allowsMove('T', col) == False:
                    col = random.choice(range(1,7))
            
            #if the new column isn't a replay col, the loop will break, otherwise it will be done at the beginning of the loop

            if self.checkLastBeadReplayTop(col) == False:
                self.makeMove('T', col)

    ##LEVEL 1 AI: will always play a replay move (one iteration), and then will play whatever valid move is in the game

    def replayCheckerTOP(self):
        '''More of a tool than acc. but plays large role in lvl One AI, this is a replay checker for the top (to see if a certain move will cause a replay), and it is necessary to account for replay rule '''
        LC = []
        QC = []

        for col in range(1,7):
            if self.allowsMove('T', col):
                if self.checkLastBeadReplayTop(col) == True:
                    LC.append(col)
                else:
                    QC.append(col)
        
        return LC, QC

    def lvlOneAI(self):
        'Level One AI: will always play a replay move where it exists, otherwise will play a random move'

        #this will put valid moves that fulfill the replay into LC (for ONE ITERATION), all other valid moves will be put into QC
        LC, QC = self.replayCheckerTOP()
        PC = sorted(LC)
        if len(LC) > 0:  
            #have to use the minimum because its the leftmost pot, otherwise the
            self.lvlOneAIReplayLoop(PC, QC) 
            if self.checkEmpty() == True:
                return
            elif len(QC) > 0:
                RC = random.choice(QC)
                self.makeMove('T', RC)
                print('I moved', RC)
            else:
                if self.checkEmpty() == True:
                    return
                else:
                    LC = [[self.allowsMove('T', col), col] for col in range(1,7)]
                    newpick = max(LC)
                    print('i am moving', newpick[1])
                    self.makeMove('T', newpick[1])
        elif len(QC) > 0:
            RC = random.choice(QC)
            self.makeMove('T', RC)
            print('I moved', RC)    

    def lvlOneAIReplayLoop(self, PC, QC):
        '''acc. of lvlOneAI, used in case of a replay'''
        #the first loop with PC
        LC, QC = self.replayCheckerTOP()
        PC = sorted(LC)
        for x in PC:
            print('i am moving', x, 'now because of last bead rule')
            self.makeMove('T', x)
            

#this is gonna be level 2 AI, and it will be mostly non-random

#this one will work by seeing which move gives the highest increase in pot beads after playing all beads that replay, after that it should just play a random bead
    def lvlTwoAI(self):
        '''this AI will go through all of the columns and see which will lead to the greatest increase in victory pot, prior to that however, it will run the moves that will give it replay'''        
        #b2 becommes the new template that b will copy off o

        QC = []
        QCReplay = []
        LC = []

        for col in range(1,7):
            if b.allowsMove('T', col):
                QC.append(col)
        
        #this is where you begin checking the columns in QC
        #first is the replay loops
        for col in QC:
            if b.checkLastBeadReplayTop(col):
                QCReplay.append(col)
                FC = sorted(QCReplay)
                #this will go low to top as to not impact the replay of other beads
                for col in FC:
                    print('I am moving', col)
                    b.makeMove('T', col)
                    print(b)
                    if self.checkEmpty():
                        return   
        #this makes the move, checks the difference in the new pot, and then reverts the board to what it was before
            else:
                self.OneCopy()

                b.makeMove('T', col)
                LC.append([b.data[1][0]-b2.data[1][0], col])

                b.OneCopyReverse()

        #this is where you run through the replays and then run through the rest
        
        ActMoveList = max(LC)
        print('I am moving', ActMoveList[1])
        b.makeMove('T', ActMoveList[1])

    #Players
    def BottomPlayer(self):
        '''This is the function for the bottom player in PVP, it takes input and makes moves based on the input'''
        #take the input as itself
        column1 = input('what column would you (BOTTOM) like to pick? ')
                    
        #check if the move is allowed
        if self.allowsMove('B', column1) == False:
            column1 = 0
            while self.allowsMove('B', column1) == False:
                print("that doesn't work")
                column1 = input("choose another ")

        newcol = int(column1)


        #go into the replay loop
        if self.checkLastBeadReplayBottom(newcol): 
                self.beadReplayLoopBot(newcol)
        #make the move if replay rule doesn't apply
        else:
            self.makeMove('B', int(newcol))

    def TopPlayer(self):
        '''This is for the TOP Player in the PVP, normally defauls to the bottom player'''
        #take the input as itself
        column1 = input('what column would you (TOP) like to pick? ')
                    
        #check if the move is allowed
        if self.allowsMove('T', column1) == False:
            column1 = 0
            while self.allowsMove('T', column1) == False:
                print("that doesn't work")
                column1 = input("choose another ")

        newcol = int(column1)


        #go into the replay loop
        if self.checkLastBeadReplayTop(newcol): 
                self.beadReplayLoopTOP(newcol)
        #make the move if replay rule doesn't apply
        else:
            self.makeMove('T', int(newcol))


#############
# game host #
#############

    def hostGame(self):
        '''runs the game of mancala'''
        Bottom = 0
        Top = 0
        choice = 0

        #Player vs. Player Option
        while choice != '9':
            self.menu()
            choice = input("how would you like to play? ")

            if choice == '0':
                print('player vs player mode')
                print(self)
                while self.checkEmpty() == False:
                    self.BottomPlayer()

                    print(self)

                    if self.checkEmpty():
                        break

                    self.TopPlayer()

                    if self.checkEmpty():
                        break

                    print(self)

                print("game over")
                winner = self.checkWin()

                if winner == 'T':
                    Top += 1
                elif winner == 'B':
                    Bottom += 1
            
            if choice == '1':
                print('player vs random ai mode')
                print(self)

                while self.checkEmpty() == False:
                    self.BottomPlayer()

                    print(self)

                    if self.checkEmpty():
                        break

                    self.randomAI()

                    print(self)

                print("game over")

                winner = self.checkWin()

                if winner == 'T':
                    Top += 1
                elif winner == 'B':
                    Bottom += 1

            if choice == '2':
                print('player vs level 1 ai (replay AI)')
                print(self)
                while self.checkEmpty() == False:
                    self.BottomPlayer()

                    print(self)

                    if self.checkEmpty():
                        break

                    self.lvlOneAI()

                    print(self)

                print("game over")
                winner = self.checkWin()

                if winner == 'T':
                    Top += 1
                elif winner == 'B':
                    Bottom += 1

            if choice == '3':
                print('player vs level 2 ai (most points AI)')
                print(self)
                while self.checkEmpty() == False:
                    self.BottomPlayer()

                    print(self)

                    if self.checkEmpty():
                        break

                    self.lvlTwoAI()
                    
                    print(self)

                print("game over")
                winner = self.checkWin()

                if winner == 'T':
                    Top += 1
                elif winner == 'B':
                    Bottom += 1

            if choice == '8':
                print("Score")
                print('Top:', Top)
                print('Bottom:', Bottom)

                if Top > Bottom:
                    print('Top is winning by', Top - Bottom)
                elif Top < Bottom:
                    print('Bottom is winning by', Bottom - Top)
                else:
                    print('score is currently tied')

            self.reset()

        print("Final Score")
        print('Top:', Top)
        print('Bottom:', Bottom)

        if Top > Bottom:
            print('Top won by', Top - Bottom)
        elif Top < Bottom:
            print('Bottom won by', Bottom - Top)
        else:
            print('Tie')
             
b = Board(8,2)
b2 = Board(8,2)
b3 = Board(8,2)

b.hostGame()


#boards to copy to 
