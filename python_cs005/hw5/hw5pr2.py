#hw5pr2.py
#pranav patel

def numToBaseB(N, B):
    '''usage: numToBaseB(Number (in decimal), B); converts decimal number to Base B'''
    remainder = N % B 

    if N == 0:
        return ''

    else:
        return  numToBaseB(N//B, B) + str(remainder)

def baseBToNum(S, B):
    ''' usage: baseBToNum(S, B): converts string S in base B to decimal '''
    if S == '':
        return 0

    # if the last digit is a '1'...
    
    else: 
        lastdigit = int(S[-1])
        return (B * baseBToNum(S[:-1], B)) + lastdigit

def baseToBase(B1, B2, s_in_B1):
    '''usage: baseToBase(B1, B2, s_in_B1) converts string S_in_B1 in base B1 to base B2'''
    LC = baseBToNum(s_in_B1, B1)
    return numToBaseB(LC, B2)

def add(S, T):
    PC = baseBToNum(S, 2)
    LC = baseBToNum(T, 2)

    AD = PC + LC

    return numToBaseB(AD, 2)


def addB(S, T):
    """usage: addB(S, T) adds binary strings S and T"""
    # base cases!
    def addhelper(S, T, C):
        if S == '' and T == '':
            if C == 1:
                return '1'
            elif C == 0:
                return ''

        elif S == '' and T != '':
            if C == 1:
                return addhelper('1', T, 0)
            elif C == 0:
                return T
        
        elif S != '' and T == '':
            if C == 1:
                return addhelper(S, '1', 0)
            elif C == 0:
                return S

        elif S[-1] == '0' and T[-1] == '0':
            if C == 0:
                return addhelper(S[:-1], T[:-1], 0) + '0'  
            elif C == 1:
                return addhelper(S[:-1], T[:-1], 0) + '1'   

        elif S[-1] == '0' and T[-1] == '1':
            if C == 0:
                return addhelper(S[:-1], T[:-1], 0) + '1'  
            elif C == 1:
                return addhelper(S[:-1], T[:-1], 1) + '0'   

        elif S[-1] == '1' and T[-1] == '0':
            if C == 0:
                return addhelper(S[:-1], T[:-1], 0) + '1'  
            elif C == 1:
                return addhelper(S[:-1], T[:-1], 1) + '0'   

        elif S[-1] == '1' and T[-1] == '1':
            if C == 0:
                return addhelper(S[:-1], T[:-1], 1) + '0'  
            elif C == 1:
                return addhelper(S[:-1], T[:-1], 1) + '1'

    return addhelper(S, T, 0)   
        
def compress(I):
    '''usage compress(binarystring); takes binary string I and losslessly compresses in 8-bit strings where 1st number is the binary number and remaining 7 represent amount of times it exists in a row'''
    if I == '':
        return ''

    elif I[0] == '1':
        q = frontNum(I)
        bq = numToBaseB(q, 2)
        finalbq = (7 - len(bq)) * '0' + bq
        return '1' +  finalbq + compress(I[frontNum(I):])

    elif I[0] == '0':
        q = frontNum(I)
        bq = numToBaseB(q, 2)
        finalbq = (7 - len(bq)) * '0' + bq
        return '0' + finalbq + compress(I[frontNum(I):])


def frontNum(L):
    '''helperfunc for compress: indicates ammount of times the first character of a string is repeated'''
    if len(L) == 0:
        return 0
    
    elif len(L) == 1:
        return 1

    elif L[1] == L[0]:
        return 1 + frontNum(L[1:])
    
    else:
        return 1

def uncompress(C):
    '''usage: uncompress(compressedstring), uncompresses a string in 8-bit lossless compression'''
    if C == '':
        return ''
    
    else:
       return C[0]*baseBToNum(C[1:8], 2) + uncompress(C[8:])
        

