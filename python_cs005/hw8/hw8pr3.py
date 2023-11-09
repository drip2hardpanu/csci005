import random
import math

def dart():
    """Throws one dart between (-1,-1) and (1,1).
       Returns True if it lands in the unit circle; otherwise, False.
    """
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    if x**2 + y**2 < 1:
        return True  # HIT (within the unit circle)
    else:
        return False # missed (landed in one of the corners)

def forpi(n):
    """Throws N darts, estimating pi."""
    pi = 4     # A suitably poor initial estimate
    throws = 0  # No throws yet 
    hits = 0    # No "hits" yet  (hits ~ in the circle

    for x in range(n):
        throws += 1 
        if dart() == True:
            hits += 1
            newpi = float(hits)/float(throws) * float(pi)
            print(str(hits) + " hit out of " + str(throws) + " throws so that pi is " + str(newpi)) 
            return newpi
        
        elif dart() == False:
            hits += 0
            newpi = float(hits)/float(throws) * float(pi)
            print(str(hits) + " hit out of " + str(throws) + " throws so that pi is " + str(newpi)) 
            return newpi
    

def whilepi(error):
    '''Usage: whilepi(error)
    This program will keep return the amount of trials needed in throwing darts randomly at a dartboard until abs((4 * hits/throws)-pi) < error
    '''
    pi = 4     # A suitably poor initial estimate
    throws = 0  # No throws yet 
    hits = 0    # No "hits" yet  (hits ~ in the circle

    toss = dart()
    if toss == True:
        throws = 1
        hits = 1 
    
    elif toss == False:
        throws = 1 
        hits = 0
    
    newpi = hits/throws * pi

    while abs(newpi-math.pi) > error:
        toss = dart()

        if toss == True:
            hits += 1
            throws += 1 
            newpi = hits/throws * pi
            print(str(hits) + " hit out of " + str(throws) + " throws so that pi is " + str(newpi)) 

        elif toss == False:
            hits += 0
            throws += 1
            newpi = hits/throws * pi 
            print(str(hits) + " hit out of " + str(throws) + " throws so that pi is " + str(newpi)) 

    return throws



def forpi_np(n):
    """Throws N darts, estimating pi.
    NO PRINTING"""
    pi = 4     # A suitably poor initial estimate
    throws = 0  # No throws yet 
    hits = 0    # No "hits" yet  (hits ~ in the circle

    for x in range(n):
        throws += 1
        if dart() == True:
            hits += 1
        
        elif dart() == False:
            hits += 0

    return pi*hits/throws




def whilepi_np(error):
    '''Usage: whilepi(error)
    This program will keep return the amount of trials needed in throwing darts randomly at a dartboard until abs((4 * hits/throws)-pi) < error
    NO PRINTING
    '''
    pi = 4     # A suitably poor initial estimate
    throws = 0  # No throws yet 
    hits = 0    # No "hits" yet  (hits ~ in the circle

    toss = dart()
    if toss == True:
        throws = 1
        hits = 1 
    
    elif toss == False:
        throws = 1 
        hits = 0
    
    newpi = hits/throws * pi

    while abs(newpi-math.pi) > error:
        toss = dart()

        if toss == True:
            hits += 1
            throws += 1 
            newpi = hits/throws * pi

        elif toss == False:
            hits += 0
            throws += 1
            newpi = hits/throws * pi 

    return throws
"""
LC = [forpi_np(n) for x in range(1000)]

average for n=1 in forpi = 3.152
[4.0, 4.0, 0.0, 4.0, 0.0, 4.0, 4.0, 4.0, 4.0, 4.0, 0.0, 4.0, 4.0, 0.0, 4.0, 0.0, 0.0, 4.0]

average for n = 10 in forpi = 3.151199999999986
[4.0, 4.0, 4.0, 3.6, 2.8, 3.2, 3.2, 2.4, 2.8, 3.2, 3.2, 3.2, 3.2, 3.2, 3.6, 3.6, 3.2, 3.6]

average for n = 100 in forpi = 3.14471999999999
[3.08, 3.08, 3.04, 3.16, 3.16, 3.32, 2.84, 3.16, 3.16, 3.08, 3.4, 3.16, 3.36, 3.2, 2.96, 3.08, 3.2, 3.12]

average for n = 1000 in forpi = 3.141367999999997
[3.192, 3.088, 3.2, 3.136, 3.144, 3.084, 3.1, 3.172, 3.14, 3.116, 3.228, 3.184, 3.148, 3.088, 3.052, 3.088, 3.14, 3.132]

LC = [whilepi_np(error) for x in range(1000)]

average for error = 1 in whilepi is 1.826
[1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 7]

average for error = .1 in whilepi is 33.565
[9, 13, 5, 5, 34, 5, 17, 13, 506, 30, 19, 5, 13, 157, 30, 9, 5, 5]

average for error = .01 in whilepi is 432.02
[14, 83, 98, 160, 530, 33, 332, 14, 153, 199, 14, 1305, 153, 174, 132, 660, 51, 14]

average for error = .001 in whilepi is 15522.53
[1793, 219, 275, 149, 177, 219, 191, 17682, 16224, 36780, 1659367, 149, 29086, 596, 1476, 149, 135, 419]

Does forpi or whilepi estimate pi more efficiently, why?
Whilepi doesn't really estimate pi, rather it just counts the iterations of forpi needed to get to a certain error; If I had to, I would argue that forpi is more efficient because it doesn't have an unbounded iteration number. Theoretically, its possible for whilepi to go on indefinitely whereas forpi will go until n = 0. Looking back, I didn't have to use a while loop, i could've definitely just used a for loop.... oh well.

While pi will estimate it more accurately, granted the value of pi is built into whilepi, however, its ability to iterate indefinitely is also a plus because the focus isn't necessarily on n, rather its on the accuracy of the estimation. That's why the input is an error and not an amoutn of iterations. 

"""
