# CS5 Gold, hw2pr2
# Filename: hw2pr2.py
# Name: Pranav Patel
# Problem description: Sleepwalking student

import random 
from random import * 
import emoji


def rs():
    """rs chooses a random step and returns it.
       Note that a call to rs() requires parentheses.
       Arguments: none at all!
    """
    return choice([-1, 0, 1])

import time

def rwpos(start, nsteps):
    """ rwpos models a random walker that
        * starts at the int argument, start
        * takes the int # of steps, nsteps

        rwpos returns the final position of the walker.
    """
    time.sleep(0.1)
    print('location is', start)
    if nsteps == 0:
        return start
    else:
        newpos = start + rs()  # take one step
        return rwpos(newpos, nsteps - 1)

import time

def rwsteps(start, low, high):
    """ rwsteps models a random walker that
        * starts at the int argument, start  
        * goes UNTIL reaching low or high
          (low will always be less than high)

        rwsteps returns the number of steps the
        walker needed to reach the lower or upper bound
    """
    time.sleep(0.05)

    if start <= low or start >= high:
        print("_"*((high-low)+1))
        return 0

    else:
        print( "_"*(start-low) + 'S' + "_"*(high-start) )
        newpos = start + rs()   # take one step, from start to newpos!
        return 1 + rwsteps(newpos, low, high)

def bumpy(p1, p2):
    """
        This simulator observes two blindfolded students, wandering about a bridge, but the bridge is floating meaning they are surrounded by cliffs on both sides. 
        will they find eachother, or will they fall off??

        sA:  the location of the first student (who wanders)
        PT:  the location of the poptart (it does not move)
        sB:  the location of the second student (who wanders)   
        
        The endpoints are always at 0 and 30. To start,  0 < sA < PT < sB < 30

        Good values to run:  poptart_royale(5, 10, 15)  # evenly spaced
                                poptart_royale(5, 20, 30)  # uneven spacing: sB is closer...
    """ 

    #extra credit emojis

    #extra credit terminal colors    
    time.sleep(0.05)

    if p1 < 0 or p2 > 30: #ends game if you go over 30 or under 0
        print('game over, you fell off')
        return 0
    
    elif p2 <= p1: #ends game if you hit eachother
        together = emoji.emojize(":couple_with_heart:")
        print("cliff"+"\033[6;30;47m" + "_"*(p1+1) + "\033[0m" + together + "\033[6;30;47m" + "_"*(30-(p2-1)) + "\033[0m"+"cliff") 
        print('you found eachother!!')
        return 0

    else:
        newpos1 = p1 + rs() # take one step, from start to newpos!
        if newpos1 < p1:
            kendrick = emoji.emojize(":person_walking:")
        elif newpos1 == p1:
            kendrick = emoji.emojize(":person_standing:")
        else:
            kendrick = emoji.emojize(":person_walking:")
                
        newpos2 = p2 + rs()
        if newpos2 < p2:
            walter = emoji.emojize(":person_walking:")
        elif newpos2 == p2:
            walter = emoji.emojize(":person_standing:")
        else:
            walter = emoji.emojize(":person_walking:")

        print("cliff"+"\033[6;30;47m" + "_"*(p1) + "\033[0m" + "\033[6;31;45m" + kendrick + "\033[0m" + "\033[6;30;47m" + "_"*(p2-p1) + "\033[0m" + "\033[6;31;45m" + walter + "\033[0m" + "\033[6;30;47m" + "_"*(30-p2) + "\033[0m"+"cliff") 
        return 1 + bumpy(newpos1, newpos2)

    """
    example run

cliff________🧍_________🚶_____________cliff
cliff________🧍__________🚶____________cliff
cliff________🚶_________🚶_____________cliff
cliff_________🧍_________🚶____________cliff
cliff_________🚶__________🚶___________cliff
cliff__________🧍________🚶____________cliff
cliff__________🚶_________🚶___________cliff
cliff_________🧍___________🚶__________cliff
cliff_________🚶__________🧍___________cliff
cliff________🧍___________🧍___________cliff
cliff________🧍___________🚶___________cliff
cliff________🚶____________🚶__________cliff
cliff_______🚶____________🚶___________cliff
cliff______🚶______________🧍__________cliff
cliff_____🧍_______________🧍__________cliff
cliff_____🚶_______________🧍__________cliff
cliff____🚶________________🧍__________cliff
cliff_____🧍_______________🧍__________cliff
cliff_____🚶_______________🚶__________cliff
cliff____🚶_________________🧍_________cliff
cliff___🚶__________________🧍_________cliff
cliff____🚶_________________🚶_________cliff
cliff_____🚶_________________🚶________cliff
cliff____🧍_________________🚶_________cliff
cliff____🧍________________🚶__________cliff
cliff____🧍_________________🚶_________cliff
cliff____🧍________________🚶__________cliff
cliff____🧍_______________🧍___________cliff
cliff____🚶_______________🚶___________cliff
cliff_____🧍_____________🚶____________cliff
cliff_____🚶____________🚶_____________cliff
cliff____🧍____________🚶______________cliff
cliff____🚶_____________🚶_____________cliff
cliff___🚶_______________🧍____________cliff
cliff____🚶______________🚶____________cliff
cliff___🚶______________🚶_____________cliff
cliff____🧍______________🚶____________cliff
cliff____🚶_______________🧍___________cliff
cliff___🧍________________🚶___________cliff
cliff___🚶_________________🧍__________cliff
cliff____🚶________________🚶__________cliff
cliff___🚶__________________🚶_________cliff
cliff__🚶__________________🚶__________cliff
cliff___🚶________________🧍___________cliff
cliff__🧍_________________🚶___________cliff
cliff__🧍________________🚶____________cliff
cliff__🚶_______________🚶_____________cliff
cliff_🚶_______________🚶______________cliff
cliff🚶_______________🧍_______________cliff
cliff_🚶______________🧍_______________cliff
cliff__🧍_____________🚶_______________cliff
cliff__🧍______________🚶______________cliff
cliff__🚶_______________🚶_____________cliff
cliff_🚶_________________🚶____________cliff
cliff🧍_________________🧍_____________cliff
cliff🧍_________________🚶_____________cliff
cliff🚶__________________🚶____________cliff
cliff_🚶________________🚶_____________cliff
cliff🚶__________________🚶____________cliff
cliff_🚶__________________🚶___________cliff
cliff__🧍__________________🚶__________cliff
cliff__🧍_________________🧍___________cliff
cliff__🚶_________________🚶___________cliff
cliff_🚶___________________🚶__________cliff
cliff🧍___________________🚶___________cliff
cliff🚶__________________🚶____________cliff
game over, you fell off
Out[8]: 66

    example run 2:

In [10]: bumpy(8,17)
cliff________🚶_________🚶_____________cliff
cliff_______🧍_________🚶______________cliff
cliff_______🚶__________🚶_____________cliff
cliff________🧍________🚶______________cliff
cliff________🚶_________🧍_____________cliff
cliff_________🧍________🚶_____________cliff
cliff_________🚶_______🧍______________cliff
cliff__________🚶______🧍______________cliff
cliff___________🚶_____🧍______________cliff
cliff__________🧍______🧍______________cliff
cliff__________🧍______🚶______________cliff
cliff__________🚶_____🚶_______________cliff
cliff_________🧍_____🚶________________cliff
cliff_________🧍______🧍_______________cliff
cliff_________🧍______🚶_______________cliff
cliff_________🚶_____🧍________________cliff
cliff__________🧍____🧍________________cliff
cliff__________🧍____🚶________________cliff
cliff__________🚶_____🚶_______________cliff
cliff___________🚶___🚶________________cliff
cliff____________🚶___🚶_______________cliff
cliff___________🧍_____🚶______________cliff
cliff___________🚶____🚶_______________cliff
cliff__________🧍____🚶________________cliff
cliff__________🧍___🧍_________________cliff
cliff__________🚶___🚶_________________cliff
cliff___________🚶___🧍________________cliff
cliff__________🚶____🚶________________cliff
cliff___________🚶__🚶_________________cliff
cliff_____________💑___________________cliff
you found eachother!!
Out[10]: 29

    """