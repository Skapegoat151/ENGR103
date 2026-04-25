#######################################################################
# Program Filename: hw3
# Author: Connor Irwin
# Date: 4/24/2026
# Description: Completes the task outlined in ENGR103_HWK3_QualityControl-2
# Input: measures of interest, desired sample average value, desired standard deviation value
# Output: Average sample value, lower and upper bounds of standard deviation for sample, desired sample average compared to range
#######################################################################



#######################################################################
# Function: make_float
# Description: makes sure that the user inputs a number for their measured value
# Parameters: num1 = input value, num2 = which item the measured value is for
# Return values: num1 as a float
# Pre-Conditions:
# Post-Conditions:
#######################################################################

def make_float(num1):
    while isinstance(num1, str):
        try:
            num1 = float(num1)
        except:
            print("Please enter only numbers\nEnter the appropriate value:", end=" ")
            num1 = input()

    return float(num1)



#######################################################################
# Function: above_zero
# Description: makes sure that the number input is greater than 0
# Parameters: num1 = float input value, num2 = which item the measured value is for
# Return values: num1 as a float > 0
# Pre-Conditions:
# Post-Conditions:
#######################################################################

def above_zero(num1):
    num1 = make_float(num1)
    while num1 <= 0:
        print("Please enter only numbers greater than 0\nEnter the appropriate value:", end=" ")
        num1 = input()
        num1 = make_float(num1)

    return num1



#######################################################################
# Function: main
# Description: the main program
# Parameters: none
# Return values: lower and upper bound, actual average
# Pre-Conditions:
# Post-Conditions:
#######################################################################

def main():
    moi = [0, 0, 0, 0, 0]

    #get all measures of interest
    i = 0
    while i < 5:
        print("Enter the measured value for item", i+1, "in the sample:", end=" ")
        temp = input()
        moi[i] = above_zero(temp)
        i += 1

    #get goal values
    print("Enter the goal average value:", end=" ")
    goalAve = above_zero(input())
    print("Enter the goal standard deviation value:", end=" ")
    goalSD = above_zero(input())

    #do calculations
    calcAve = sum(moi)/5
    lb = goalAve - (3 * goalSD) / (5 ** (1 / 2))
    ub = goalAve + (3 * goalSD) / (5 ** (1 / 2))

    #print results
    print("\nLower bound:", format(lb, ".2f"))
    print("Calculated average: ", format(calcAve, ".2f"))
    print("Upper bound: ", format(ub, ".2f"), "\n")

    if calcAve > ub:
        print("WARNING! The sample average is ABOVE the expected range!\n")
    elif calcAve < lb:
        print("WARNING! The sample average is BELOW the expected range!\n")
    else:
        print("All good! The sample average is within the expected range.\n")


main()