import random

#######################################################################
# Function: input_function
# Description: Gets a number from 1 to 10 and makes sure it is valid
# Parameters: N/A
# Return values: The guessed number
# Pre-Conditions:
# Post-Conditions:
#######################################################################

def input_function():
    check = True
    while check == True:
        guess = input("Guess a whole number from 1 to 10: ")
        try:
            guess = int(guess)
            if guess < 1 or guess > 10:
                print("Please only enter numbers from 1 to 10")
            else:
                check = False
        except:
            print("Please only enter whole numbers")
    
    return guess


#######################################################################
# Function: guess_checker
# Description: Checks if the guessed number is equal to the generated number
# Parameters: guess = the guessed number, num = the correct number
# Return values: prints results
# Pre-Conditions:
# Post-Conditions:
#######################################################################

def guess_checker(num):
    guess = input_function()
    correct = False
    tries = 0
    while tries < 4 and correct == False:
        if guess == num:
            correct = True
        else:
            tries += 1
            print("I'm sorry that is incorrect you have", 5 - tries, "tries left.")
            guess = input_function()
    
    if correct == True:
        print("Congratulations you got it right!\n It took you", tries + 1, "guesses.")
    else:
        print("I'm sorry you ran out of guesses, the correct number is", num)


#######################################################################
# Function: main
# Description: generates a number and the user guesses it
# Parameters: N/A
# Return values: N/A
# Pre-Conditions:
# Post-Conditions:
#######################################################################

def main():
    num = random.randint(1, 10)
    print(num)
    guess_checker(num)


main()