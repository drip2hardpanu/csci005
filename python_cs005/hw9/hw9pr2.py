#
# hw9pr2.py
#
# Name: Pranav Patel
#

# Here is a function for printing 2D arrays
#  (lists-of-lists) of data

def print2d(A):
    """print2d prints a 2D array, A,
       as rows and columns.
       Argument: A, a 2D list of lists.
       Result: None (no return value)
    """
    num_rows = len(A)
    num_cols = len(A[0])

    for r in range(num_rows):
        for c in range(num_cols):
            print(A[r][c], end = ' ')
        print()

    print()

    return None  # This is implied anyway
                 # when no return statement is present

def createA(num_rows, num_cols, s):
    """Returns a 2D array with
           num_rows rows and
           num_cols columns
       using the data from s: across the
       first row, then across the second, etc.
       We'll only test it with enough data!
    """
    A = []
    for r in range(num_rows):
        newrow = []
        for c in range(num_cols):
            newrow += [s[0]] # Add that char
            s = s[1:]        # Get rid of that first char
        A += [newrow]
    return A

def inarow_3east(ch, r_start, c_start, A):
    '''usage: inarow_3east(ch, r_start, c_start, A)
    checks for three-in-a-row eastward of element ch at A[r_start][c_start]'''
    try:
        A[r_start][c_start+2]
    except:
        return False

    LC = []
    for c in range(3):
        if ch == A[r_start][c_start+c]:
            LC.append(True)
        else:
            LC.append(False)
    
    return min(LC)
            


def inarow_3south(ch, r_start, c_start, A):
    '''usage: inarow_3south(ch, r_start, c_start, A)
    checks for three-in-a-row southward of element ch at A[r_start][c_start]'''
    try:
        A[r_start+2][c_start]
    except:
        return False

    LC = []
    for c in range(3):
        if ch == A[r_start+c][c_start]:
            LC.append(True)
        else:
            LC.append(False)
    
    return min(LC)


##def inarow_3southeast(ch, r_start, c_start, A):
def inarow_3southeast(ch, r_start, c_start, A):
    '''usage: inarow_3southeast(ch, r_start, c_start, A)
    checks for three-in-a-row southeast of element ch at A[r_start][c_start]'''
    try:
        A[r_start+2][c_start+2]
    except:
        return False

    LC = []
    for c in range(3):
        if ch == A[r_start+c][c_start+c]:
            LC.append(True)
        else:
            LC.append(False)
    
    return min(LC)


##def inarow_3northeast(ch, r_start, c_start, A):\

def inarow_3northeast(ch, r_start, c_start, A):
    '''usage: inarow_3northeast(ch, r_start, c_start, A)
    checks for three-in-a-row northeast of element ch at A[r_start][c_start]'''
    try:
        A[r_start-2][c_start+2]
    except:
        return False

    LC = []
    for c in range(3):
        if ch == A[r_start-c][c_start+c]:
            LC.append(True)
        else:
            LC.append(False)
    
    return min(LC)

def threeinrowtest():
    # tests of inarow_3east
    A = createA(3, 4, 'XXOXXXOOOOOO')
    print("\n3east :")
    print2d(A)
    assert inarow_3east('X', 0, 0, A) == False
    assert inarow_3east('O', 2, 1, A) == True
    assert inarow_3east('X', 2, 1, A) == False
    assert inarow_3east('O', 2, 2, A) == False
    print("All 3east tests worked!")

    # tests of inarow_3south
    A = createA(4, 4, 'XXOXXXOXXOO OOOX')
    print("\n3south :")
    print2d(A)
    assert inarow_3south('X', 0, 0, A) == True
    assert inarow_3south('O', 2, 2, A) == False
    assert inarow_3south('X', 1, 3, A) == False
    assert inarow_3south('O', 42, 42, A) == False
    print("All 3south tests worked!")

    # tests of inarow_3southeast
    A = createA(4, 4, 'XOOXXXOXX XOOOOX')
    print("\n3southeast :")
    print2d(A)
    assert inarow_3southeast('X', 1, 1, A) == True
    assert inarow_3southeast('X', 1, 0, A) == False
    assert inarow_3southeast('O', 0, 1, A) == True
    assert inarow_3southeast('X', 2, 2, A) == False
    print("All 3southeast tests worked!")

    # tests of inarow_3northeast
    A = createA(4, 4, 'XOXXXXOXXOXOOOOX')
    print("\n3northeast :")
    print2d(A)
    assert inarow_3northeast('X', 2, 0, A) == True
    assert inarow_3northeast('O', 3, 0, A) == True
    assert inarow_3northeast('O', 3, 1, A) == False
    assert inarow_3northeast('X', 3, 3, A) == False
    print("All 3northeast tests worked!")

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


def Ninrowtest():
    A = createA(5, 5, 'XXOXXXOOOOOOXXXX XXXOOOOO')
    print("\nNeast :")
    print2d(A)
    assert inarow_Neast('O', 1, 1, A, 4) == True
    assert inarow_Neast('O', 1, 3, A, 2) == True
    assert inarow_Neast('X', 3, 2, A, 4) == False
    assert inarow_Neast('O', 4, 0, A, 5) == True
    print("All Neast tests worked!")

    A = createA(5, 5, 'XXOXXXOOOOOOXXXXOXXXOOOXO')
    print("\nNsouth :")
    print2d(A)
    assert inarow_Nsouth('X', 0, 0, A, 5) == False
    assert inarow_Nsouth('O', 1, 1, A, 4) == True
    assert inarow_Nsouth('O', 0, 1, A, 6) == False
    assert inarow_Nsouth('X', 4, 3, A, 1) == True
    print("All Nsouth tests worked!")

    A = createA(5, 5, 'XOO XXXOXOOOXXXXOXXXOOOXX')
    print("\nNsoutheast :")
    print2d(A)
    assert inarow_Nsoutheast('X', 1, 1, A, 4) == True
    assert inarow_Nsoutheast('O', 0, 1, A, 3) == False
    assert inarow_Nsoutheast('O', 0, 1, A, 2) == True
    assert inarow_Nsoutheast('X', 3, 0, A, 2) == False
    print("All Nsoutheast tests worked!")

    A = createA(5, 5, 'XOO XXXOXOOOXOXXXOXXXOOXX')
    print("\nNnortheast :")
    print2d(A)
    assert inarow_Nnortheast('X', 4, 0, A, 5) == True
    assert inarow_Nnortheast('O', 4, 1, A, 4) == True
    assert inarow_Nnortheast('O', 2, 0, A, 2) == False
    assert inarow_Nnortheast('X', 0, 3, A, 1) == False
    print("All Nnortheast tests worked!")
