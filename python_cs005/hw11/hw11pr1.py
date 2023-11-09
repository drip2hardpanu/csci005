
Web VPython 3.2
# for Trinket glowscript, you need the line    GlowScript 3.2 VPython

#
# game_starter.py
#
# Building an interaction with 3D graphics using Python
#   Documentation: http://www.glowscript.org/docs/VPythonDocs/index.html
#   Examples:      http://www.glowscript.org/#/user/GlowScriptDemos/folder/Examples/
#

scene.bind('keydown', keydown_fun)     # Function for key presses
scene.bind('click', click_fun)         # Function for mouse clicks
scene.background = 0.8*vec(1, 1, 1)    # Light gray (0.8 out of 1.0)
scene.width = 640                      # Make the 3D canvas larger
scene.height = 480


# +++ start of OBJECT_CREATION section
# These functions create "container" objects, called "compounds"

def make_alien(starting_position, starting_vel = vec(0, 0, 0)):
    """The lines below make a new "frame", which is a container with a
       local coordinate system.
       The arguments to make_alien allow for any initial starting position
       and initial starting velocity, with a default starting velocity
       of vec(0, 0, 0).

       Compounds can have any number of components.  Here are the
       alien's components:
    """
    alien_body = sphere(size = 1.0*vec(1, 1, 1),
                        pos = vec(0, 0, 0),
                        color = color.green
                        )
    alien_eye1 = sphere(size = 0.3*vec(1, 1, 1),
                        pos = .42*vec(.7, .5, .2),
                        color = color.white
                        )
    alien_eye2 = sphere(size = 0.3*vec(1, 1, 1),
                        pos = .42*vec(.2, .5, .7),
                        color = color.white
                        )
    alien_hat = cylinder(pos = 0.42*vec(0, .9, -.2),
                         axis = vec(.02, .2, -.02),
                         size = vec(0.2, 0.7, 0.7),
                         color = color.magenta
                         )

    # Make a list to "fuse" with a compound
    alien_objects = [alien_body, alien_eye1, alien_eye2, alien_hat]

    # Now, we create a compound--we'll name it com_alien:
    #
    com_alien = compound(alien_objects,
                         pos = starting_position
                         )
    com_alien.vel = starting_vel    # Set the initial velocity
    return com_alien



# The ground is represented by a box (vPython's rectangular solid)
# http://www.glowscript.org/docs/VPythonDocs/box.html
#
ground = box(size = vec(20, 1, 20),
             pos = vec(0, -1, 0),
             color = .4*vec(1, 1, 1))

# Create two walls, also boxes
#
wallA = box(pos = vec(0, 0, -10),
            axis = vec(1, 0, 0),
            size = vec(20, 1, .2),
            color = vec(1.0, 0.7, 0.3)  # Amber
            )
wallB = box(pos = vec(-10, 0, 0),
            axis = vec(0, 0, 1),
            size = vec(20, 1, .2),
            color = color.blue          # Blue
            )
            
wallC = box(pos = vec(0, 0, 10),
            axis = vec(-1, 0, 0),
            size = vec(20, 1, .2),
            color = color.green          # green
            )
wallD = box(pos = vec(10, 0, 0),
            axis = vec(0, 0, -1),
            size = vec(20, 1, .2),
            color = color.red          # green
            )
            
block = box(size=vector(2,2,2), 
            pos = vec(2,0,0),
            color=color.orange)



# Create a ball that we will be able to cocntrol
#
ball = sphere(size = 1.0*vec(1, 1, 1),  # Ball is an object of class sphere
              color = vec(0.8, 0.5, 0.0)
              )
ball.vel = vec(0, 0, 0)                 # This is its initial velocity

# We make two aliens using two calls to the make_alien function (from above)
#
alien1 = make_alien(starting_position = vec(6, 0, -6),
                    starting_vel = vec(0, 0, -1))
alien2 = make_alien(starting_position = vec(-10, 5, -10))
                                        # Zero starting velocity for alien2


# +++ end of OBJECT_CREATION section


# +++ start of ANIMATION section

# Other constants
#
RATE = 30                # The number of times the while loop runs each second
dt = 1.0/(1.0*RATE)      # The time step each time through the while loop
scene.autoscale = False  # Avoids changing the view automatically
scene.forward = vec(0, -3, -2)  # Ask for a bird's-eye view of the scene...

# This is the "event loop" or "animation loop"
# Each pass through the loop will animate one step in time, dt
#
while True:

    rate(RATE)                              # Maximum number of times per second
                                            # ..that the while loop runs

    # +++ Start of PHYSICS UPDATES -- update all positions here, every time step

    alien1.pos = alien1.pos + alien1.vel*dt # Update the first alien's position
    ball.pos = ball.pos + ball.vel*dt       # Update the ball's position

    # +++ End of PHYSICS UPDATES -- be sure new objects are updated appropriately!

    corral_collide(ball)
    corral_collide(alien1)
    
    
#block = box(size=vector(2,2,2), 
            #pos = vec(2,0,0),
            #color=color.orange)
            
    if mag(ball.pos - block.pos) < 2.0:
        ball.vel *= -1.0
    
    if mag(alien.pos - block.pos) < 2.0:
        alien.vel *= -1.0

            
    # If the ball collides with the first alien, give the alien
    # a vertical velocity
    if mag(ball.pos - alien1.pos) < 1.0:
        print("To infinity and beyond!")
        alien1.color = color.gray(.8)
        alien1.vel = vec(0, 1, 0)

    # If the first alien ventures too far, restart randomly--but only if it's
    # not moving vertically.
    if mag(alien1.pos) > 10  and  alien1.vel.y < 1:
        alien1.pos.x = choice([-6, 6])
        alien1.pos.z = choice([-6, 6])
        alien1.vel = 2*vec.random()        # Library-supplied random vector
        alien1.vel.y = 0.0                 # No vertical component of velocity

    # +++ End of COLLISIONS



# +++ Start of EVENT-HANDLING section--separate functions for
#                                keypresses and mouse clicks...

def keydown_fun(event):
    """This function is called each time a key is pressed."""
    # ball.color = randcolor()  # This turns out to be very distracting!
    key = event.key
    ri = randint(0, 10)
    print("key:", key, ri)      # Prints the key pressed--caps only...

    amount = 0.42               # "Strength" of the keypress's velocity changes
    if key == 'up' or key in 'wWiI':
        ball.vel = ball.vel + vec(0, 0, -amount)
    elif key == 'left' or key in 'aAjJ':
        ball.vel = ball.vel + vec(-amount, 0, 0)
    elif key == 'down' or key in 'sSkK':
        ball.vel = ball.vel + vec(0, 0, amount)
    elif key == 'right' or key in "dDlL":
        ball.vel = ball.vel + vec(amount, 0, 0)
    elif key in ' rR':
        ball.vel = vec(0, 0, 0) # Reset! via R or the spacebar, " "
        ball.pos = vec(0, 0, 0)

def click_fun(event):
    """This function is called each time the mouse is clicked."""
    print("event is", event.event, event.which)

# +++ End of EVENT-HANDLING section
def corral_collide(ball):
    """Corral collisions!
       Ball must have a .vel field and a .pos field.
    """

    # If the ball hits wallA
    if ball.pos.z < wallA.pos.z:           # Hit--check for z
        ball.pos.z = wallA.pos.z           # Bring back into bounds
        ball.vel.z *= -1.0                 # Reverse the z velocity

    # If the ball hits wallB
    if ball.pos.x < wallB.pos.x:           # Hit--check for x
        ball.pos.x = wallB.pos.x           # Bring back into bounds
        ball.vel.x *= -1.0                 # Reverse the x velocity

    # If the ball hits wallB
    if ball.pos.z > wallC.pos.z:           # Hit--check for x
        ball.pos.z = wallC.pos.z           # Bring back into bounds
        ball.vel.z *= -1.0                 # Reverse the x velocity

    if ball.pos.x > wallD.pos.x:           # Hit--check for x
        ball.pos.x = wallD.pos.x           # Bring back into bounds
        ball.vel.x *= -1.0                 
        

# +++ Other functions can go here...

def choice(L):
    """Implements Python's choice using the random() function."""
    LEN = len(L)                        # Get the length
    randomindex = int(LEN*random())     # Get a random index
    return L[randomindex]               # Return that element

def randint(low, hi):
    """Implements Python's randint using the random() function.
       returns an int from low to hi _inclusive_ (so, it's not 100% Pythonic)
    """
    if hi < low:
        low, hi = hi, low               # Swap if out of order!
    LEN = int(hi) - int(low) + 1.       # Get the span and add 1
    randvalue = LEN*random() + int(low) # Get a random value
    return int(randvalue)               # Return the integer part of it

def randcolor():
    """Returns a vector of (r, g, b) random from 0.0 to 1.0."""
    r = random()           # This is different than Python's random.uniform
    g = random()           # ..it automatically uses 0.0 to 1.0
    b = random()
    return vec(r, g, b)                 # A color is a three-element vector

