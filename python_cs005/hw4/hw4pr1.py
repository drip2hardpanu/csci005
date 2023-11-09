#hw4pr1.py
#Pranav Patel

def encipher(s, N):
    '''usage: encipher(string, rotational number)
    encipher will take the string and rotate each letter by the rotational number, like the ceasarian cipher
    note: non alphabetical characters will stay the same, uppercase letter will yeild uppercase output and vice versa'''

    def helperfunc(x, N):
        '''helper function for encipher, will rotate each letter accordingly'''

        if ord(x) >= 97 and ord(x) <= 122:
            dec = ord(x)
            if dec + N <= 122:
                rotated = dec + N
                return chr(rotated)
            elif dec + N >= 122:
                newN = dec + N - 123
                return helperfunc('a', newN)

        elif ord(x) >= 65 and ord(x) <= 90:
            dec = ord(x)
            if dec + N <= 90:
                rotated = dec+N
                return chr(rotated)
            elif dec + N >= 90:
                newN = ord(x) + N - 123
                return encipher('a', newN)

        else:
            return x
        
    LC = [helperfunc(x, N) for x in s]
    PC = ''.join(LC)
    return PC

def letterScore(let):
    """usage: letterScore(let) where let is a letter; will return the scrabble letter value"""

    ones ='aAEeIilLOoUuTtNnRrsSuU'
    twos ='dGgG'
    threes = 'bBcCmMpP'
    fours = 'fFhHvVwWyY'
    fives ='Kk'
    eights = 'jJxX'
    tens ='qQzZ'

    if let[0] in tens:
        return 10

    elif let[0] in ones:
        return 1

    elif let[0] in twos:
        return 2

    elif let[0] in threes:
        return 3

    elif let[0] in fours:
        return 4

    elif let[0] in fives:
        return 5

    elif let[0] in eights:
        return 8
    
    else:
        return 0

def scrabbleScore(S):
    """usage: scrabbleScore(S) where S is a string, returns the cumulative scrabble word score of the string"""
    if S == '':
        return 0
    
    else:
        product = letterScore(S[0])
        return product + scrabbleScore(S[1:])

def decipher(s):
    '''usage: decipher(string)
    runs encipher iterations through the whole alphabet and returns the iteration with the lowest cumulative scrabble score'''
    LC = [encipher(s, N) for N in range(26)]
    PC = [[scrabbleScore(x), x] for x in LC]
    minPC = min(PC)
    return minPC[1]

def blsort(L):
    '''indexes a list, if the element equals 0 it is added to the beginning of the list and if it equals 1 it is added to the end of the list'''
    if L == []:
        return []

    elif L[0] == 1:
        return blsort(L[1:]) + [1]
    
    elif L[0] == 0:
        return [0] + blsort(L[1:]) 

def gensort(L):
    if L == []:
        return []
    
    elif float(L[0]) == float(min(L)):
        return L[0:1] + gensort(L[1:])
    
    else:
        newlist = L[1:] + L[0:1]
        return gensort(newlist)

def jscore(S,T):
    '''usage: jscore(string1, string2) indexes a list and returns the number of characters both lists share'''
    if S == '':
        return 0
    
    elif T == '':
        return 0

    if S[0] in T:
        if S[0] == T[0]:
            return 1 + jscore(S[1:], T[1:])

        else:
            return 0 + jscore(S, T[1:] + T[0])
            
    else:
        return 0 + jscore(S[1:], T)

def exact_change(target_amount, L):
    '''usage: exact_change(amount, list of digits) returns true or false depending on if there are elements in the list of digits that can be added up to create amount) 
'''
    if target_amount == 0:
        return True
    
    elif target_amount < 0:
        return False
    
    elif L == []:
        return False

    use = exact_change(target_amount - L[0], L[1:])
    lose =  exact_change(target_amount, L[1:])

    return use or lose


def LCS(S, T):
    '''usage: LCS(string1, strin2) returns longest substring shared by both S and T
'''
    if S == '':
        return ''
    
    elif T == '':
        return ''
    
    elif S[0] == T[0]:
        return S[0] + LCS(S[1:], T[1:])

    list = []
    
    result1 = LCS(S[1:], T)
    loseit = ''.join(result1)
    list.append(loseit)
    
    result2 = LCS(S , T[1:])
    useit = ''.join(result2)
    list.append(useit)

    PC = [[len(x), x] for x in list]
    LC = max(PC)
    return LC[1]


def exact_change(target_amount, L):
    '''usage: exact_change(amount, list of digits) returns true or false depending on if there are elements in the list of digits that can be added up to create amount) 
'''
    if target_amount == 0:
        return True
    
    elif target_amount < 0:
        return False
    
    elif L == []:
        return False

    use = exact_change(target_amount - L[0], L[1:])
    lose =  exact_change(target_amount, L[1:])

    return use or lose

def helper(target_amount, L, N):
    if N == 0:
        return []

    else:
        Q = len(L)
        PC = [[exact_change(target_amount, L.pop(i)), L] for i in range(Q)]
        QC = PC.remove(False)
        LC = [x[2] for x in QC]
        print(LC)
        return LC + helper(target_amount, LC, N-1)