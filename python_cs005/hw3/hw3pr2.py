# CS 5 Gold, hw3pr2
# filename: hw3pr2.py
# Name: Pranav Patel
# problem description: List comprehensions

# this gives us functions like sin and cos...
from math import *



# two more functions (not in the math library above)

def dbl(x):
    """Doubler!  argument: x, a number"""
    return 2*x

def sq(x):
    """Squarer!  argument: x, a number"""
    return x**2

# examples for getting used to list comprehensions...

def lc_mult(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each multiplied by 2**
    """
    return [2*x for x in range(N)]

def lc_idiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       WARNING: this is INTEGER division...!
    """
    return [x//2 for x in range(N)]

def lc_fdiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       NOTE: this is floating-point division...!
    """
    return [x/2 for x in range(N)]

# printing tests
print( "lc_mult(4)   should be [0, 2, 4, 6] :", lc_mult(4) )   
print( "lc_idiv(4)   should be [0, 0, 1, 1] :", lc_idiv(4) ) 
print( "lc_fdiv(4)   should be [0.0, 0.5, 1.0, 1.5] :", lc_fdiv(4) ) 

# assertion tests
assert lc_mult(4) == [0, 2, 4, 6]
assert lc_idiv(4) == [0, 0, 1, 1]
assert lc_fdiv(4) == [0.0, 0.5, 1.0, 1.5]

# Here is where your functions start for the lab:

# Step 1, part 1
def unitfracs(N):
    """Be sure to improve this docstring!
    """
    return [float(x/N) for x in range(N)]

def scaledfracs(low, high, N):
    """usage: scaledfracs(low, high, N)
        splits the interval into N equally spaced units
    """
    factor =(high-low)/N
    return[low + x*(factor) for x in range(N)]

#step 2, part 1
def sqfracs(low, high, N):
    """usage: sqfracs(low, high, N)
        splits the interval into N equally spaced units and squares every value
    """
    return[x**2 for x in scaledfracs(low, high, N)]

#step 2, part 2
def f_of_fracs(f, low, high, N):
    """usage: f_of_fracs(f, low, high, N):
        splits the interval into N equally spaced units and runs function (f) on each term
    """
    return[f(x) for x in scaledfracs(low, high, N)]

#step 3, part 1
def integrate(f, low, high, N):
    """Integrate returns an estimate of the definite integral
       of the function f (the first argument)
       with lower limit low (the second argument)
       and upper limit high (the third argument)
       where N steps are taken (the fourth argument)

       integrate simply returns the sum of the areas of rectangles
       under f, drawn at the left endpoints of N uniform steps
       from low to high
    """
    factor =(high-low)/N
    return sum([factor*x for x in f_of_fracs(f, low, high, N)])

"""Q1 
Since the y-value of functions are measured at the leftmost x-value, this function will underestimate increasing functions and overestimate decreasing functions; 2x is a linearly increasing function, meaning as n approaches infinity (and as the interval x-values approach 0), the sum will approach the true area under the curve (in our case 100) but it will always underestimate it. It will overestimate -2x.
"""
def c(x):
    """c is a semicircular function of radius two"""
    return (4 - x**2)**0.5

"""Q2

a. 3.732050807568877
b. 3.228464879754982
c. 3.1511769448395257
d. 3.1425795059119648

As N goes to infinity, the area under the curve approaches pi; the equation for the area of this circle is 4pi, and every 1/4th of it (fourth was taken from our function) would be pi.
"""
