
################################################
# Function: calc_and_print
# Description: calculates the total gallons of gas used and how much money was spent on that gas and prints it out
# Parameters: The cost per gallon of gas, 
# Return values: prints the total gallons used, and total spent on gas
# Pre-Conditions:
# Post-Conditions:
################################################

def calc_and_print(mpg, gasCost):
    galUsed = 100000 / gasCost
    spent = mpg * galUsed

    print("Total gallons used: ", galUsed)
    print("Total spent of gas", spent)


################################################
# Function: main
# Description: gathers input and calls calc_and_print
# Parameters: none
# Return values: none
# Pre-Conditions:
# Post-Conditions:
################################################

def main():
    mpg = float(input("MPG:  "))
    gas_cost = float(input("Cost of gas: "))

    calc_and_print(mpg, gas_cost)


main()

# adds 2 numbers
def add(num1, num2):
    print("The sum is ", num1 + num2)

add(7, 6)



