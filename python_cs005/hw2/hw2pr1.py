#hw2pr1.py
#task1

from turtle import *

t = Turtle()

t.shape('turtle')  # or 'arrow'

t.speed(10)  # fastest speed!

t.color("green")
t.width(4)
t.forward(100)
t.left(60)

t.color("blue")
t.width(4)
t.forward(100)
t.left(60)

t.color("green")
t.width(4)
t.forward(100)
t.left(60)

t.color("blue")
t.width(4)
t.forward(100)
t.left(60)

t.color("green")
t.width(4)
t.forward(100)
t.left(60)

t.color("blue")
t.width(4)
t.forward(100)
t.left(60)

#task2

from turtle import *
t = Turtle()

def tri(n):
    """Draws n 100-pixel sides of an equilateral triangle.
       Note that n doesn't have to be 3 (!)
    """
    
    t.pensize(10)
    clr = input(['darkgreen', 'red'])
    t.pencolor(clr) 
  
    if n == 0:
        t.forward(100)
        return      # No sides to draw, so stop drawing
    else:
        t.dot(10, 'red') 
        t.forward(100)
        t.left(120)
        tri(n-1)    # Recur to draw the rest of the sides!

#
# here, run tri(3)   
#
t.fillcolor('cyan')
t.begin_fill()
tri(2)
t.end_fill()

#task 3 
from turtle import *

t = Turtle()

t.speed(10)  # 10 is the fastest speed...

def spiral(initialLength, angle, multiplier):
    """Spiral-drawing function.  Arguments:
       initialLength = the length of the first leg of the spiral
       angle = the angle, in degrees, turned after each spiral's leg
       multiplier = the fraction by which each leg of the spiral changes
    """
    if initialLength <= 1 or initialLength > 1000:
        return      # No more to draw, this base case stops the recursion
    else:
        t.forward(initialLength)
        t.left(angle)
        spiral( initialLength*multiplier  , angle  , multiplier )  # What inputs?!

#
spiral(100, 60, 0.99)   # here, call spiral!
#

#task 4
from turtle import * 

t = Turtle()

t.penup()
t.backward(150)
t.pendown()

from turtle import * 

t = Turtle()

t.penup()
t.backward(150)
t.pendown()

def svtree(trunklength, levels):
    """svtree: draws a side-view tree
       trunklength = the length of the first line drawn ("the trunk")
       levels = the depth of recursion to which it continues branching
    """
    if levels == 0:
        t.fillcolor('red')
        t.begin_fill()
        t.circle(4)
        t.end_fill()
        return
    
    else:
        # Draw the original trunk (1 line)
        t.forward(trunklength)
        # Turn a little bit to position the first subtree (1 line)
        t.left(45)
        # Recurse! with both a smaller trunk and fewer levels (1 line)
        svtree(trunklength/2,levels-1)
        
        # Turn the other way to position the second subtree (1 line)
        t.right(90)
        # Recurse again! (1 line)
        svtree(trunklength/2,levels-1)

        # Turn a little bit to position the first subtree (1 line)
        t.left(45)
        # Recurse! with both a smaller trunk and fewer levels (1 line)
        svtree(trunklength/2,levels-1)

        # Turn and go BACKWARDS (2 steps: 2 lines)
        t.backward(trunklength)
        return # delete this empty statement later
      
svtree(100, 3)

#task 5

from turtle import *

t = Turtle()

def snowflake(sidelength, levels):
    """Fractal snowflake function, complete.
       sidelength: pixels in the largest-scale triangle side
       levels: the number of recursive levels in each side
    """
    flakeside(sidelength, levels)
    t.left(120)
    flakeside(sidelength, levels)
    t.left(120)
    flakeside(sidelength, levels)
    t.left(120)

def flakeside(sidelength, levels):
    """ flakeside draws _one side_ of the fractal Koch snowflake
    """
    if levels == 0:
      t.forward(sidelength)
      return
    
    else:
        flakeside(sidelength/3,levels-1)
      
        t.right(60)
    
        flakeside(sidelength/3,levels-1)
        
        t.left(120)
        
        flakeside(sidelength/3,levels-1)
        
        t.right(60)
        
        flakeside(sidelength/3,levels-1)  
        return
    
t.penup()
t.goto(-200,-100)  # move the pen to a "southwest" corner...
t.pendown()
snowflake(300,2)   # two recursive levels deep!

