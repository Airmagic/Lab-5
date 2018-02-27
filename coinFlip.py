# some of the code i got from stackoverflow

# importing random to get a random number
import random

# main program so I can call it
def main():
    # this try is incase a value error
    try:

        # printing what the program is and what to do
        print("Guessing the number of times heads will land.\nPut in the number of flips and then the number of times head will show.")

        # creating the variables to hold a count for them
        heads, tails, timesflipped = 0, 0, 0

        # getting the number of flips from user
        numberFlipped = numberFlippedInput()

        # getting the number of guess for heads
        guessHeads = guessHeadsInput(numberFlipped)

        # a while loop to get the number of random 0 or 1s
        while timesflipped < numberFlipped:

            # making a variable that gets a number like flipping the coin
        	coin_flips = random.randrange( 2 )

            # if statement to add numbers to that variables heads or tales
        	if coin_flips == 0:
        		heads += 1
        	else:
        		tails += 1
            # adding 1 to the variable timesFlipped
        	timesflipped += 1
        # if statement if you guessed correct or not
        if heads == guessHeads:
            print("You guess correct!!!")
        else:
            print("Your guess was wrong")

        # printing the results for the user
        print("In " + str(numberFlipped) + " flips, " + str(heads) + " were heads and " + str(tails) + " were tails.")
        print("Your guess was " + str(guessHeads) + " times that heads would appear")

        # added a replay feature
        replay()



    # value error handler incase user puts in anthing other than a number
    except ValueError:
        print("Must be a number")
        # calling main program
        main()

def numberFlippedInput():
    try:
        # getting user input
        numberFlipped = int(input('How many time do you want to flip? '))
        # returning the number inputed
        return numberFlipped

    # exception if a number isn't inputed
    except ValueError:
        # print information for the user
        print("Must be a number")
        # calling main program
        numberFlippedInput()

def guessHeadsInput(number):
    try:
        # getting input from the user
        guessHeads = int(input("How many times do you think it will land heads? "))
        # checking the range so that the user puts in a plasible number
        if guessHeads < 0 or guessHeads > number:
            # printing info for the user
            print("Please enter a number from 0 to {}".format(number,))
            # returning to this program
            guessHeadsInput(number)

        # returning that variable
        return guessHeads


    except ValueError:
        print("Must be a number")
        # calling main program
        guessHeadsInput(number)


def replay():
    # asking user if they want to run the program again
    replay = input('Would you like to play again? Y or N  ')
    # if statement to open the coinFlip again if these are entered
    if replay in ('y', 'Y', 'Yes', 'YES'):
        # calling the main again
        main()
    else:
        # closing the program
        exit()

# calling the program at the end of the python so that it checks the program first
if __name__ == '__main__':
    main()
