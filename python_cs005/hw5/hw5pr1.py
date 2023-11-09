#hw5pr1.py

def isOdd(N):
    '''usage: isOdd(number); returns true or false depedning on if number is odd'''
    if N % 2 == 1:
        return True
    
    else:
        return False

def numToBinary(N):
    '''usage: numToBinary(number); converts number to binary string '''
    if N == 0:
        return ''
    elif N%2 == 1:
        return  numToBinary(N//2) + '1'
    else:
        return  numToBinary(N//2) + '0'

def binaryToNum(S):
    '''usage: binaryToNum(string); converts binary string to number'''
    if S == '':
        return 0

    # if the last digit is a '1'...
    elif S[-1] ==  '1':
        return (2 * binaryToNum(S[:-1])) + 1 

    else: # last digit must be '0'
        return (2 * binaryToNum(S[:-1])) + 0


def increment(s):
    '''usage: increment(binarystring); increases binary string by 1'''
    number = binaryToNum(s)
    binary = numToBinary(number+1)

    length = len(binary)
    F = 8 - length

    newbinary = F*'0' + binary

    if len(newbinary) > 8:
        trim = len(newbinary) - 8
        return newbinary[trim:]
    
    else:
        return newbinary

def count(s, N):
    '''usage: count(binarystring, N)); increases binary string by N'''
    if N == 0:
        print(s)

    else:
        print(s)
        count(increment(s), N-1) 
        
def numToTernary(N):
    '''usage: numToTernary(number); converts decimal number to ternary string'''
    if N == 0:
        return ''

    elif N % 3 == 2:
        return  numToTernary(N//3) + '2'

    elif N % 3 == 1:
        return  numToTernary(N//3) + '1'

    else:
        return  numToTernary(N//3) + '0'

def ternaryToNum(S):
    '''usage: ternarytoNum(string); converts ternary string to decimal number'''
    if S == '':
        return 0

    # if the last digit is a '1'...
    elif S[-1] ==  '1':
        return (3 * ternaryToNum(S[:-1])) + 1 
    
    elif S[-1] ==  '2':
        return (3 * ternaryToNum(S[:-1])) + 2 
    
    else: # last digit must be '0'
        return (3 * ternaryToNum(S[:-1])) + 0

def balancedTernaryToNum(S):
    '''usage: balancedTernaryToNum(string); converts balanced ternary string to decimal number'''    
    if S == '':
        return 0

    FC = []
    for x in S:
        if x == '+':
            FC.append(1) 
        elif x == '-':
            FC.append(-1) 
        elif x == '0':
            FC.append(0) 

    N = len(FC)

    PC = [[len(FC)-1 - i, FC[i]] for i in range(N)]

    LC = [x[1]*3**x[0] for x in PC]

    return sum(LC)

def numToBalancedTernary(N): 
    '''usage: numToBalancedTernary(N); converts decimal number to balanced ternary string'''    
    if N == 0:
        return ''
    elif N % 3 == 1: 
        return numToBalancedTernary(N// 3) + '+' 
    elif N % 3 == 2:
        return numToBalancedTernary(N // 3 + 1) + '-'
    else:
        return numToBalancedTernary(N // 3) + '0'
