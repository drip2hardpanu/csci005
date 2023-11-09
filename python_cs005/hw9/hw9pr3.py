
#
# Example user-interaction looping program
#  (a variant of the one done in class)
#

def menu():
    """Prints the menu of options that the user can choose."""
    print()
    print("(0) Input a new list") #seems fine
    print("(1) Print the current list") #seems fine
    print("(2) Find the average price") #seems fine
    print("(3) Find the standard deviation") #seems finee
    print("(4) Find the minimum price and its day")
    print("(5) Find the maximum price and its day")
    print("(6) Your TT investment plan")
    print("(9) Break! (quit)") #DONE
    print()

def predict(L):
    """Predict ignores its argument and returns
       what the next element should have been.
    """
    return 42

#############################################################
################# MATH HELPER FUNCS #########################

def find_min(L):
    """find min uses a loop to return the minimum of L.
       Argument L: a nonempty list of numbers.
       Return value: the smallest value in L.
    """
    result = L[0]
    for x in L:
        if x < result:     # A smaller one was found!
            result = x
    return result

def find_min_loc(L):
    """find min loc uses a loop to return the minimum of L
            and the location (index or day) of that minimum.
        Argument L: a nonempty list of numbers.
        Results:  the smallest value in L, its location (index)
    """
    minval = L[0]
    minloc = 0

    for i in list(range(len(L))):
        if L[i] < minval:  # A smaller one was found!
            minval = L[i]
            minloc = i

    return minval, minloc

def find_max_loc(L):
    """find max loc uses a loop to return the maximum of L
            and the location (index or day) of that maximum.
        Argument L: a nonempty list of numbers.
        Results:  the biggest value in L, its location (index)
    """
    maxval = L[0]
    maxloc = 0

    for i in list(range(len(L))):
        if L[i] > maxval:  # A larger one one was found!
            maxval = L[i]
            maxloc = i

    return maxval, maxloc
#############################################################
#############################################################

def main():
    """The main user-interaction loop."""
    secret_value = 4.2

    L = [30, 10, 20]  # an initial list

    while True:       # The user-interaction loop
        menu()
        choice = input("Choose an option: ")

        #
        # "Clean and check" the user's input
        # 
        try:
            choice = int(choice)   # Make into an int!
        except:
            print("I didn't understand your input! Continuing...")
            continue

        #
        # Run the appropriate menu option
        #
        if choice == 9:    # We want to quit 
            break          # Leaves the while loop altogether

        elif choice == 1:  # We want to continue (and print) ...
            LC = [[L[i], i] for i in range(len(L))]
            QC = [["Day", "Price"]] + LC

            for list in QC:
                d = list[1]
                p = list[0]
                print(f"{d:>4} : $ {p:>6}")
            continue       # Goes back to the top of the while loop,
                           # ..where it will print L

        elif choice == 0:  # We want to enter a new list
            newL = input("Enter a new list: ")    # Enter _something_
            
            
            # "Clean and check" the user's input
            #
            try: 
                newL = eval(newL) # eval runs Python's interpreter! Note: Danger!
                if type(newL) != type([]): 
                    print("That didn't seem like a list. Not changing L.")
                else: 
                    L = newL  # Here, things were OK, so let's set our list, L
            except:
                print("I didn't understand your input. Not changing L.")

        elif choice == 2:  # average
            sum = 0
            length = 0

            for x in L:
                sum += x
            for x in L:
                length += 1
            
            av = sum/length
            print("The average price is", av)

        elif choice == 3:  # standard deviation
            rum = 0
            length = 0
            sdsum = 0

            for x in L:
                rum += x
            for x in L:
                length += 1
            
            av = rum/length
            QC = [(x - av) for x in L]
            for x in QC:
                sdsum += x**2
        
            sumlen = sdsum/length
            sd = sumlen**.5

            print("The standard deviation is", sd)

        elif choice == 4:  # Unannounced menu option (more interesting...)
            minval, minloc = find_min_loc(L)
            print("The minimum value is ", minval, "on day ", minloc)

        elif choice == 5:  # Even more interesting unannounced menu option...
            maxval, maxloc = find_max_loc(L)
            print("The maximum value in L is", maxval, "at day #", maxloc)
        
        elif choice == 6:
            LC = []

            for b in range(len(L)):
                for s in range(b, len(L)):
                        LC.append([L[b]-L[s], b, s])
            
            bigdiff = min(LC)
            print("buy on day ", bigdiff[1], "at ", L[bigdiff[1]] )
            print("sell on day ", bigdiff[2], "at ", L[bigdiff[2]] )
            print("For a profit of ", abs(bigdiff[0]))

        else:
            print(choice, " ?      That's not on the menu!")
            continue

    print()
    print("See you yesterday!")