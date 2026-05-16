import sys

#######################################################################
# Program Filename: hw4
# Author: Connor Irwin
# Date: 5/12/2026
# Description: Completes the task outlined in ENGR103_HWK4_LearningCurves-2
# Input: 
# Output: 
#######################################################################


#######################################################################
# Function: error_check
# Description: makes sure that the user inputs a number for their measured value
# Parameters: userInput = the input given by the user
#             ask = what to ask the user to enter in case they do not enter a number
# Return values: userInput as a float
# Pre-Conditions:
# Post-Conditions:
#######################################################################
def error_check(userInput, ask):
    # Loop until userInput can be made into a float
    check = True
    while check == True:
        try:
            userInput = float(userInput)

            check = False
        except:
            print("Your input is not a number. Try again!")
            userInput = input(ask)
    # Returns userInput as a float
    return userInput

#######################################################################
# Function: big_enough
# Description: makes sure the inputs necessary inputs are greater than 0
# Parameters: userInput = the input given by the user
#             ask = what to ask the user to enter in case they do not enter a number
# Return values: userInput as a float greater than 0
# Pre-Conditions:
# Post-Conditions:
#######################################################################
def big_enough(userInput, ask):
    # Make sure userInput is a number
    userInput = error_check(userInput, ask)
    
    # Make sure userInput is greater than 0
    check = True
    while check == True:
        if userInput < 0:
            print("Your input needs to be greater than 0. Try again!")
            userInput = input(ask)
            userInput = error_check(userInput, ask)
        else:
            check = False

    # Returns userInput as a float greater than 0
    return userInput


#######################################################################
# Function: cycle_loop
# Description: loops through the decreasing cycle time until the desired time is reached or the user quits
# Parameters: goalTime = the goal cycle time
#             cycleTime = the cycle time for the current iteration
#             slope = the slope for the decrease in cycle time
# Return values: none but prints the cycle time for each iteration
# Pre-Conditions:
# Post-Conditions:
#######################################################################
def cycle_loop(goalTime, cycleTime, slope):
    # Counts every 100 to add to the current cycle when printed
    loops = 0

    # Loops through decreasing the cycle time and checking if it is lower than the goal
    while cycleTime > goalTime:
        # Loops 100 times or until the goal cycle time is reached
        for i in range(1, 101):
            print(f"Cycle: {i + loops}  {cycleTime:.3f}")
            if cycleTime < goalTime:
                print(f"The desired cycle time has been achieved!\nThe learning percent was {(100 * 2 ** slope):.0f}%")
                sys.exit()
            cycleTime = cycleTime * 2 ** slope
        # Checks if the user wants to continue after 100 cycles
        print(f"{loops + 100} cycles have been checked!")
        cont = input('Do you want to continue? Enter "n" to quit: ')
        if cont.lower() == "n":
            sys.exit()
        else:
            loops += 100

#######################################################################
# Function: main
# Description: gets the user input for the starting values, and calls other functions
# Parameters: N/A
# Return values: N/A
# Pre-Conditions:
# Post-Conditions:
#######################################################################
def main():
    # Get the goal cycle time as a number
    goalTime = input("Enter the GOAL cycle time in minutes: ")
    goalTime = big_enough(goalTime, "Enter the GOAL cycle time in minutes: ")

    # Get the first cycle time as a number
    firstTime = input("Enter the FIRST cycle time in minutes: ")
    firstTime = big_enough(firstTime, "Enter the FIRST cycle time in minutes: ")

    # Make sure the first cycle time is greater than the goal cycle time
    if goalTime > firstTime:
        print("Your GOAL cycle time must be less than your FIRST cycle time.\nStart over and try again!")
        sys.exit()

    # Get the slope as a number less than 0
    slope = input("Enter the slope as a number less than 0: ")
    slope = error_check(slope, "Enter the slope as a number less than 0: ")
    while slope > 0:
        print("Your slope must be less than 0. Try again!")
        slope = input("Enter the slope as a number less than 0: ")
        slope = error_check(slope, "Enter the slope as a number less than 0: ")

    # Takes the input values and loops them to find the goal cycle time
    cycle_loop(goalTime, firstTime, slope)

main()