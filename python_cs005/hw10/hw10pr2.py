
def inarow_Neast(ch, r_start, c_start, A, N):
    '''usage: inarow_Neast(ch, r_start, c_start, A, N)
    checks for three-in-a-row east of element ch at A[r_start][c_start]'''
    try:
        A[r_start][c_start+(N-1)]
    except:
        return False

    LC = []
    for c in range(N):
        if ch == A[r_start][c_start+c]:
            LC.append(True)
        else:
            LC.append(False)
    
    return min(LC)

def inarow_Nsouth(ch, r_start, c_start, A, N):
    '''usage: inarow_Nsouth(ch, r_start, c_start, A, N)
    checks for three-in-a-row south of element ch at A[r_start][c_start]'''
    try:
        A[r_start+(N-1)][c_start]
    except:
        return False

    LC = []
    for c in range(N):
        if ch == A[r_start+c][c_start]:
            LC.append(True)
        else:
            LC.append(False)
    
    return min(LC)

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    '''usage: inarow_Nsoutheast(ch, r_start, c_start, A, N)
    checks for three-in-a-row southeast of element ch at A[r_start][c_start]'''
    try:
        A[r_start+(N-1)][c_start+(N-1)]
    except:
        return False

    LC = []
    for c in range(N):
        if ch == A[r_start+c][c_start+c]:
            LC.append(True)
        else:
            LC.append(False)
    
    return min(LC)

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    '''usage: inarow_Nnortheast(ch, r_start, c_start, A, N)
    checks for three-in-a-row northeast of element ch at A[r_start][c_start]'''
    try:
        A[r_start-(N-1)][c_start+(N-1)]
    except:
        return False

    LC = []
    for c in range(N):
        if ch == A[r_start-c][c_start+c]:
            LC.append(True)
        else:
            LC.append(False)
    
    return min(LC)

class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        s = ''   # the string to return
        for row in range(0,self.height):
            s += '|'   
            for col in range(0,self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width+1) * '-' + '\n' #bottom of the board

        #adding numbers
        for col in range(self.width):
            s += ' ' + str(col%10)

        return s       # the board is complete, return it

    def addMove(self, col, ox):
        """usage: addMove(self, col, ox), col represents the index of the column to which the checker will be added. ox is a 1-character string representing the checker to add to the board"""
        for row in range(self.height):
            if self.data[row][col] != ' ':
                self.data[row-1][col] = ox
                return
            
        self.data[self.height-1][col] = ox

    def clear(self):
        """ clears the board by replacing all non empty spaces with empty spaces"""
        for row in range(self.height):
            for col in range(self.width):
                if self.data[row][col] != ' ':
                    self.data[row][col] = ' '
        
        return

    def setBoard(self, moveString):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.setBoard('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.setBoard('000000') to
           see them alternate in the left column.

           moveString must be a string of one-digit integers.
        """
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'

    def allowsMove(self, c):
        """usage: allowMoves(self, c), checks to see if column c is full"""
        if c < 0:
            return False
        elif c > self.width - 1 :
            return False
        elif self.data[0][c] != ' ':
            return False
        else:
            return True

    def isFull(self):
        """usage: isFull(self), checks to see if board is full"""
        LC = []
        for c in range(self.width):
            LC.append(self.allowsMove(c))
        
        if max(LC) == False:
            return True
        else:
            return False


    def delMove(self, c):
        """usage: addMove(self, col, ox), col represents the index of the column to which the checker will be added. ox is a 1-character string representing the checker to add to the board"""
        if self.allowsMove(c):
            for row in range(self.height):
                if self.data[row][c] != ' ':
                    if self.data[row-1][c] == ' ':
                        self.data[row][c] = ' '
                        return
                    elif self.data[self.height-1][c] == ' ':
                        return 
        else:
            self.data[0][c] = ' '
            return
    
    def winsFor(self, ox): 
        '''takes input of O or X, checks if there is a winning combination on the board'''

        # Check to see if ox wins, starting from any checker:
        for row in range(self.height):
            for col in range(self.width):
                if inarow_Neast(ox, row, col, self.data, 4) == True:
                    return True
                elif inarow_Nsouth(ox, row, col, self.data, 4) == True:
                    return True
                elif inarow_Nsoutheast(ox, row, col, self.data, 4) == True:
                    return True
                elif inarow_Nnortheast(ox, row, col, self.data, 4) == True:
                    return True
                # you need three more, very similar, such checks
                # for the three other directions!

        # but, if it looks at EACH row and col and never finds a win...
        return False     # only gets here if it never returned True, above


    def hostGame(self):
        '''runs the game of connect 4'''
        while self.winsFor('X') == False and self.winsFor('O') == False: 

            print(self)

            column1 = int(input("what column would X like to drop? "))

            if self.allowsMove(column1) == False:
                column1 = -1    # Note! This -1 is _intentionally_ not valid!
                while self.allowsMove(column1) == False:  # _while_ not valid
                    column1 = int(input("Choose a column: "))  # ask for a column
                self.addMove(column1, 'X')

                if self.isFull():
                    break

            else:
                self.addMove(column1, 'X')

                if self.isFull():
                    break
            
            print(self)

            column2 = int(input("what column would O like to drop?"))

            if self.allowsMove(column2) == False:
                column2 = -1    # Note! This -1 is _intentionally_ not valid!
                while self.allowsMove(column2) == False:  # _while_ not valid
                    column2 = int(input("Choose a column: "))  # ask for a column
                self.addMove(column2, 'O')

                if self.isFull():
                    break

            else:
                self.addMove(column2, 'O')

                if self.isFull():
                    break
        
        print(self)






# This is the end of the Board class
# Below are some boards that will be re-created each time the file is run:

bigb = Board(15,5)
b = Board(7,6)
