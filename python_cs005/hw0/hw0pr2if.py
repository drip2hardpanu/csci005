# coding: utf-8
#by: Pranav Patel
# hw0pr2if.py
#

""" 
Title for your adventure:   Prom Night.

Notes on how to "win" or "lose" this adventure:
    You will win as long as you don't walk and then answer anything but yes in the first 2 decisions.
"""

import time
import sys

def adventure():

    delay = 1.5          # change to 0.0 for testing or speed runs,
                         # ..larger for dramatic effect!
    def spacer():
        print()
        time.sleep(delay)

    #intro sequence 
    print('bff:its almost prom time, im so excited!') 
    spacer()
    print('as you walk into the venue, everything looks beautiful')
    print('at the bottom of the entry tale, you see the blue sparkly letters:') 
    spacer()
    print('P-R-O-M')
    spacer()
    print('walking up to the table, a chaperone greets you')
    spacer()
    print('hey, whats your name?')
    user_name = input("name: ")

    print()
    print("chaperone: you said,", user_name, "?, lemme see if I can find you on the list")
    spacer()
    print("chaperone: hmm,", user_name, user_name, user_name)
    spacer()
    print("chaperone: ...I don't see you on the list.")
    spacer()
    print("your heart races... did you buy tickets?")
    spacer()
    print("you don't know if you should point it out or walk away...")
    spacer()

    #if/elif statement {1} decision 1
    choice1 = input("what do you do? [point/walk] ")

    #1a {point}, function definition
    def point():
            spacer()
            print('you scour the list for your name')
            spacer()
            print('huzzah, you found it!')
            spacer()
            print('you point at', user_name, 'on the sheet' )

            #part 2 {wo sys exit; wasn't sure if I could use it} (this should be within the point function to ensure the program ends if the other choice is selected)
            time.sleep(delay)
            print('whew! that was a close one')
            print('the venue looks majestic')
            spacer()
            print('your bff and their date sit next to your crush and you')
            time.sleep(delay)
            print('crush: can you get me a drink?')
            spacer()
            print('you get up and walk over to the refreshments table...')
            time.sleep(delay)
            print('but all you see are some different sodas')
            time.sleep(delay)

            #decision 3 
            print('what soda do you get?')
            drink = input("drink:")

            #good soda; paired w ending
            def good():
                print("crush: ahh how did you know",drink, "was my favorite??")
                time.sleep(delay)
                print("they proceed to take a sip of the drink, and by the end of the night its gone!")

            #goodend 
            def goodend():
                time.sleep(delay)
                print('...later that night')
                spacer()
                print("you parked in front of your crush's house after driving them home")
                spacer()
                print("crush: thank you for the best night ever, I will never forget you")
                spacer()
                print("you drive home, your heart full of happiness")
                spacer()
                print("the end")

            #story keeps going on/changed to incorporate basketball storyline since wasn't ending otherwise; if elif and else statements {2b}
            def storycontinues():
                print("throughout the night, you notice your crush hasn't taken a single sip of the drink")
                spacer()
                print("you ask if the drink was bad...")
                spacer()
                print("crush: no...thank you for bringing it")
                time.sleep(delay)
                print("they take a quick sip of the drink and promptly gag")

                spacer()
                print('some time passes, and you all decide to go play some basketball')
                spacer()
                print('you 1v1 your crush')
                time.sleep(delay)

                #decision 4
                print('how many buckets are you dropping [1-20]') 
                buckets = float(input("number: "))

                #happyending 1
                def win():
                    print('you decide to take it easy on your crush and drop',buckets, 'on them')
                    spacer()
                    print('they decide to go easy on you too')
                    spacer()
                    print('on one point, you both fall down together')
                    spacer()
                    print('instead of getting up, you both lay down and watch the stars...super corny')
                    goodend()

                #lose on court--> paired with happyending2
                def lose():
                    print('you decide to prove your dominance in basketball and drop',buckets, 'on them')
                    spacer()
                    print("you still can't beat them, they block all your shots and steal the ball")
                    spacer()
                    print("on the final point they cross you over and you fall on the ground")
                    spacer()
                    print('Crush: BAM...loserrrrr! get off the court!')
                
                #happy ending 2
                def badend():
                    print('you lose basketball, even after trying...')
                    spacer()
                    print('...later that night')
                    spacer()
                    print("you parked in front of your crush's house after driving them home")
                    time.sleep(delay)
                    print("you ask them how the night was")
                    spacer()
                    print("crush: honestly...") 
                    time.sleep(delay)
                    print("tonight wasn't bad")
                    time.sleep(delay)
                    print("it was honestly really good...")
                    time.sleep(delay)
                    print("but you do suck at basketball")
                    spacer()
                    print("you drive home, determined to beat them next time ")
                    spacer()
                    print("the end")

                #tie, incorporates independent if statement
                def tie():
                    print( 'you decide to try and drop', buckets, 'on them' )
                    spacer()
                    print('they decide to try too')
                    spacer()
                    print('its the end of the game, and the score is close')
                    spacer()
                    print("you crossover your crush, and you're wide open")
                    spacer()

                    #decision 5
                    print('do you miss the shot on purpose?')
                    final = input("miss? ")

                    if final == 'yes':
                        print('you miss the shot!')
                        spacer()
                        print('as they go to block it, you both fall down together')
                        spacer()
                        print('instead of getting up, you both lay down and watch the stars...super corny')
                        spacer()
                        goodend() 

                if buckets < 5:
                    win()
                
                elif buckets < 15:
                    tie()
                
                else:
                    lose()

                    badend()


            #soda tests (good-end:coke/sprite, continue:fanta/else)[if elif elif else]{3}
            if drink == 'coke':
                print('coke is crazy, personally I wouldnt')
                spacer()
                print('you hand your crush the coke, topped with ice cubes and vanilla ice cream') #good
                good()
                goodend()

            elif drink == 'sprite':
                print('sprite... interesting choice')
                spacer()
                print('you hand your crush the sprite, topped with two ice cubes and a sour lemon slice') #good
                good() 
                goodend() 

            elif drink == 'fanta':
                print('fanta???')
                spacer()
                print('you hand your crush the fanta, topped with two ice cubes and citrusy orange slice') #bad
                storycontinues()

            else:
                print(drink, "...you're an interesting critter")
                spacer()
                print('you hand your crush the,',drink,'topped with two ice cubes and a small cherry')
                storycontinues()

    if choice1 == 'point':
        point()

    elif choice1 == 'walk':
        print('you walk away')
        spacer()
        print('...')
        
        time.sleep(delay)
        print('wait! you just saw your crush walking into the building')
       
        spacer()
        print('crush: you coming in?')

        #if else statement {decision 2}
        chance = input("are you turning around? ") 
        if chance == 'yes':
            print('you quickly turn around and begin walking towards the table again')
            point()
            
        else:
            print('you walk home, your prom night wasted...')
            spacer()
            print('as you sit in your bed... you wish you turned around')
            print('the end')