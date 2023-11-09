# coding: utf-8
# By Pranav Patel
# hw0pr2rps.py
#

import random          # imports the library named random

def rps():
    print('who dare face me in rock paper scissors?')

    #input and game begin here
    def rpsin():
        user = input("Choose your weapon: ")
        comp = random.choice(['rock', 'paper', 'scissors'])
        print()

        #actual game; cpu won't let you leave until it wins
        def choices():
            if user == 'rock' and comp == 'paper': 
                print('wow you suck')

            elif user == 'paper' and comp == 'scissors':
                print('hahaha you will never win...')
                
            elif user == 'scissors' and comp == 'rock':
                print('get off the game...')

            elif user == 'rock'  and comp == 'scissors':
                print('I meant to choose paper, double or nothing')
                rpsin()   

            elif user == 'paper' and comp == 'rock':
                print('you cheated play me again')
                rpsin()

            elif user == 'scissors' and comp == 'paper':
                print('you went early, play me again')
                rpsin()
                    
            elif user == comp:
                print('tie, play me again')
                rpsin()
        
        #checks; or function wasn't working so i split them up
        #ensures it doesn't work without proper input
        if user == 'rock':
            print('You chose', user)
            print()
            print('I chose', comp)
            choices()

        elif user == 'scissors':
            print('You chose', user)
            print()
            print('I chose', comp)
            choices()

        elif user == 'paper':
            print('You chose', user)
            print()
            print('I chose', comp)
            choices()
            
        else:
            print('that wasnt an option')
            rpsin() 
        
    rpsin()



  