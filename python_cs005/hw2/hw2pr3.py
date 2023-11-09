#hw2pr3
# Filename: hw2pr3.py
#
# Name: Pranav Patel 
# Problem description: Function Frenzy!
#

#
# vwl example from class
#
def vwl(s):
    """vwl returns the number of vowels in s
       Argument: s, which will be a string
    """
    if s == '':
        return 0   # no vowels in the empty string
    elif s[0] in 'aeiou':
        return 1 + vwl(s[1:])   # count 1 for the vowel
    else:
        return 0 + vwl(s[1:])   # The 0 + isn't necessary but looks nice

def mult(n,m):
    """  usage: multi(a,b). Gives the product of A and B """
    if m == 0:
        return 0
    elif m > 0:
        return n + mult(n, m-1)
    elif m < 0:
        return n*-1 + mult(n, m+1)

print( "mult(6, 7)           should be  42 :",  mult(6, 7) )
print( "mult(6, -7)          should be  -42 :",  mult(6, -7) )
print( "mult(-6, 7)          should be  -42 :",  mult(-6, 7) )
print( "mult(-6, -7)         should be  42 :",  mult(-6, -7) )
print( "mult(6, 0)           should be  0 :",  mult(6, 0) )
print( "mult(0, 7)           should be  0 :",  mult(0, 7) )
print( "mult(0, 0)           should be  0 :",  mult(0, 0) )

def dot(L, K):
    """usage: dot(L,K) where L and K are both lists, will return the dot product of the lists (L1*K1)+(L2*K2)..."""
    
    if len(L) != len(K) or len(L)==0 or len(K)==0:
        return 0
    
    else:
        product = float(L[0]*K[0])
        return product + dot(L[1:], K[1:])

print( "dot([5, 3], [6, 4])  should be  42.0 :",  dot([5, 3], [6, 4]) )
print( "dot([5, 3], [6])     should be  0.0 :",  dot([5, 3], [6]) )
print( "dot([], [6])         should be  0.0 :",  dot([], [6]) )
print( "dot([], [])          should be  0.0 :",  dot([], []) )
print( "dot([1, 2, 3, 4], [10, 100, 1000, 10000]) should be  43210.0 :",  dot([1, 2, 3, 4], [10, 100, 1000, 10000]) )

def ind(e, L):
    """ usage: e, L where e is an element and L is a list; function will index the list recursively and return value of list that coresponds to element.
    """
    if e not in L:
        return len(L)

    elif e == L[0]:
        return 0
    
    else:
        return 1 + ind(e, L[1:])

print( "ind(42, [55, 77, 42, 12, 42, 100]) should be  2 :",  ind(42, [55, 77, 42, 12, 42, 100]) )
print( "ind(55, [55, 77, 42, 12, 42, 100]) should be  0 :",  ind(55, [55, 77, 42, 12, 42, 100]) )
print( "ind(42, list(range(0, 100)))       should be  42 :",  ind(42, list(range(0, 100))) )
print( "ind('hi', ['hello', 42, True])     should be  3 :",  ind('hi', ['hello', 42, True]) )
print( "ind('hi', ['well', 'hi', 'there']) should be  1 :",  ind('hi', ['well', 'hi', 'there']) )
print( "ind('i', 'team')                   should be  4 :",  ind('i', 'team') )
print( "ind(' ', 'outer exploration')      should be  5 :",  ind(' ', 'outer exploration') )

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

print( "letterScore('h') should be  4 :",  letterScore('h') )
print( "letterScore('c') should be  3 :",  letterScore('c') )
print( "letterScore('a') should be  1 :",  letterScore('a') )
print( "letterScore('z') should be 10 :",  letterScore('z') )
print( "letterScore('^') should be  0 :",  letterScore('^') )

def scrabbleScore(S):
    """usage: scrabbleScore(S) where S is a string, returns the cumulative scrabble word score of the string"""
    if S == '':
        return 0
    
    else:
        product = letterScore(S[0])
        return product + scrabbleScore(S[1:])

print( "scrabbleScore('quetzal')           should be  25 :",  scrabbleScore('quetzal') )
print( "scrabbleScore('jonquil')           should be  23 :",  scrabbleScore('jonquil') )
print( "scrabbleScore('syzygy')            should be  25 :",  scrabbleScore('syzygy') )
print( "scrabbleScore('?!@#$%^&*()')       should be  0 :",  scrabbleScore('?!@#$%^&*()') )
print( "scrabbleScore('')                  should be  0 :",  scrabbleScore('') )
print( "scrabbleScore('abcdefghijklmnopqrstuvwxyz') should be  87 :",  scrabbleScore('abcdefghijklmnopqrstuvwxyz') )

def one_dna_to_rna(c):
    """Converts a single-character c from DNA
    nucleotide to its complementary RNA nucleotide
    """
    # dictionary with each conversion
    conversion = { 'A':'U', 'C':'G', 'G':'C', 'T':'A' }
    #
    # check if the input, c, is a key in the dictionary
    if c in conversion:        # is it a key?
        return conversion[c]   # if so, return its value
    else:                      # otherwise
        return ''              # return the empty string

def transcribe(S):
    """usage: transcribe(S) where S is a sequence of DNA bases; returns the transcribed version of the sequence"""
    if S == '':
        return ''
    
    else:
        transcription = one_dna_to_rna(S[0])
        return transcription + transcribe(S[1:])

print( "transcribe('ACGTTGCA')             should be  'UGCAACGU' :",  transcribe('ACGTTGCA') )
print( "transcribe('ACG TGCA')             should be  'UGCACGU' :",  transcribe('ACG TGCA') )  # Note that the space disappears
print( "transcribe('GATTACA')              should be  'CUAAUGU' :",  transcribe('GATTACA') )
print( "transcribe('cs5')                  should be  ''  :",  transcribe('cs5') ) # Note that other characters disappear
print( "transcribe('')                     should be  '' :",  transcribe('') )   # Empty strings!

# assert statements!  See below for details...
assert transcribe('ACGTTGCA') == 'UGCAACGU'
assert transcribe('ACG TGCA') == 'UGCACGU'   # Note that the space disappears
assert transcribe('GATTACA')  == 'CUAAUGU'
assert transcribe('cs5')      == ''        # Note that non-DNA other characters disappear
assert transcribe('')         == ''
