# hw8pr1.py
# Lab 8
#
# Name:
#

# keep this import line...
from cs5png3 import *

#
# A test function...
#
def test_fun():
    """Algorithmic image creation, one pixel at a time.
       This is a test function: it should create
       an image named test.png in the current directory.
    """
    im = PNGImage(300, 200)  # Creates an image of width 300, height 200

    # Nested loops!
    for r in range(200):     # loops over the rows with runner variable r
        for c in range(300): # loops over the columns with c
            if  c == r:   
                im.plotPoint(c, r, (255, 0, 0))
            #else:
            #    im.plotPoint(c, r, (255, 0, 0))
                
    im.saveFile()

#
# start your Lab 8 functions here:
#

def mult(c, n):
    """Mult multiplies c by the positive integer n,
       using only a loop and addition.
    """
    result = 0
    for i in range(n):
        result = result + c # you will write this line of code!  (Hint: add to result!)
    return result

def update(c, n):
    """Update starts with z = 0 and runs z = z**2 + c
       for a total of n times. It returns the final z.
    """
    result = 0
    for i in range(n):
        result = result**2 + c
    return result

def inMSet(c, n):
    while abs(update(c,n)) < 2:
        return True 
    else:
        return False

def weWantThisPixel(col, row):
    """This function returns True if we want to show
       the pixel at col, row and False otherwise.
    """
    if col % 10 == 0  or  row % 10 == 0:
        return True
    else:
        return False

def test():
    """This function demonstrates how
       to create and save a PNG image.
    """
    width = 300
    height = 200
    image = PNGImage(width, height)

    # Create a loop that will draw some pixels.

    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col, row):
                image.plotPoint(col, row, (255, 175, 0))

    # We looped through every image pixel; we now write the file.

    image.saveFile()

    #there wouldn't be dots, there would be lines

def scale(pix, pixMax, floatMin, floatMax):
    """scale accepts
           pix, the CURRENT pixel column (or row).
           pixMax, the total number of pixel columns.
           floatMin, the minimum floating-point value.
           floatMax, the maximum floating-point value.
       scale returns the floating-point value that
           corresponds to pix.
    """
    divisor = pix/pixMax
    diff = floatMax - floatMin
    newnum = diff * divisor + floatMin

    return newnum

def mset():
    """Creates a 300x200 image of the Mandelbrot set.
    """
    width = 300*1       # We can update the 1 later to enlarge the image...
    height = 200*1
    image = PNGImage(width, height)

    # Create a loop to draw some pixels

    for col in range(width):
        for row in range(height):
            x = scale(col, 300, -2, 1)
            y = scale(row, 200, -1, 1)
            c = x + y*1j
            n = 25
            if inMSet(c, n) == True:
                image.plotPoint(col, row, (0, 0, 0))


    # We looped through every image pixel; we now write the file
    image.saveFile()
