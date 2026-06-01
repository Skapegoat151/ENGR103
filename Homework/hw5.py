
#######################################################################
# Program Filename: hw5
# Author: Connor Irwin
# Date: 5/30/2026
# Description: Completes the task outlined in ENGR103_HWK5_Rand_Svc_Sys-1
# Input: 
# Output: 
#######################################################################


import random

# Set variables for each set attribute in a list in the order title, test, license
constants = [
    [18.63, 36.21, 5.97],
    [.3, .2, .5]
]

#######################################################################
# Function: error_check
# Description: makes sure that the user inputs a number of the right 
#              size for their entered values
# Parameters: num = the input given by the user
#             type = what type of number to set the input ass
#             ask = what to ask the user to enter in case they do not enter a number
# Return values: num as a float or int depending
# Pre-Conditions:
# Post-Conditions:
#######################################################################

def error_check(num, type, ask):
    
    # Loop until desired variable type is set
    while isinstance(num, str):
        
        # Set input to a float
        if(type == "float"):
            try:
                num = float(num)

                # Make sure input is greater than 0
                if num < 0:
                    print("Please only enter numbers greater than 0. Try again!")
                    num = input(ask)
            except:
                print("Please only enter numbers greater than 0. Try again!")
                num = input(ask)

        # Set input to an int
        else:
            try:
                num = int(num)

                # Make sure input is greater than 0
                if num < 0:
                    print("Please only enter whole numbers greater than 0. Try again!")
                    num = input(ask)
            except:
                print("Please only enter whole numbers greater than 0. Try again!")
                num = input(ask)

    return num


#######################################################################
# Function: get_input
# Description: Gets desired input from the user
# Parameters: N/A
# Return values: user input in the form of a list
# Pre-Conditions:
# Post-Conditions:
#######################################################################

def get_input():

    # Get user input
    numCustomer = input("Enter the number of customers: ")
    numCustomer = error_check(numCustomer, "int", "Enter the number of customers: ")
    numServers = input("Enter the number of DMV servers: ")
    numServers = error_check(numServers, "int", "Enter the number of DMV servers: ")
    shiftLen = input("Enter the shift length in minutes: ")
    shiftLen = error_check(shiftLen, "float", "Enter the shift length in minutes: ")

    return [numCustomer, numServers, shiftLen]


#######################################################################
# Function: assign_service
# Description: assigns each customer a dmv service id
# Parameters: inputData
# Return values: serviceData = list of each customer's assigned service
# Pre-Conditions:
# Post-Conditions:
#######################################################################

def assign_service(inputData):

    serviceData = []
    for i in range(inputData[0]):
        serviceData.append([i])

    for i in range(len(serviceData)):
        rand = random.random()
        if rand <= constants[1][0]:
            serviceData[i].append(0)
        elif rand <= (constants[1][1] + constants[1][0]):
            serviceData[i].append(1)
        else:
            serviceData[i].append(2)

    return serviceData


#######################################################################
# Function: service_time
# Description: finds each customer's service time
# Parameters: serviceData
# Return values: serviceData = list of customers, what service they want, and how long it took
# Pre-Conditions:
# Post-Conditions:
#######################################################################

def service_time(serviceData):

    # Loop through each customer
    for i in range(len(serviceData)):
        #Give each customer the appropriate time
        if serviceData[i][1] == 0:
            serviceData[i].append(constants[0][0])
        elif serviceData[i][1] == 1:
            serviceData[i].append(constants[0][1])
        else:
            serviceData[i].append(constants[0][2])

    return serviceData


#######################################################################
# Function: choose_server
# Description: chooses a server for each customer task
# Parameters: serverData
# Return values: serverData = a list of servers, their time working and time spent
# Pre-Conditions:
# Post-Conditions:
#######################################################################

def choose_server(serverData):

    # Loop through servers finding the one with the least amount of time worked
    multiple = False
    lowestTime = [serverData[0][0]]
    for i in range(len(serverData)):
        if serverData[i][1] < serverData[lowestTime[0]][1]:
            lowestTime = [serverData[i][0]]
            multiple = False
        elif serverData[i][1] == serverData[lowestTime[0]][1]:
            lowestTime.append(serverData[i][0])
            multiple = True
    
    # If there is a tie for least time worked randomly choose one server
    if multiple == True:
        divider = 1 / len(lowestTime)
        check = random.random()
        for i in range(len(lowestTime)):
            if check > (divider * i) and check < (divider + (divider * i)):
                return lowestTime[i]


#######################################################################
# Function: server_utilization
# Description: finds each server's service time
# Parameters: serviceData, serverData, shift time
# Return values: 
# Pre-Conditions:
# Post-Conditions:
#######################################################################

def server_utilization(serviceData, serverData, shiftTime):
    
    # Loop through each customer and their service time to assign a server and add that to server time
    for i in range(len(serviceData)):
        serviceData[i].append(choose_server(serverData))
        serverData[serviceData[i][3]][1] += serviceData[i][3]

    # Find server utilization percentage
    for i in range(len(serverData)):
        serverData[i].append(serverData[i][1] / shiftTime)

    return[serviceData, serverData]



#######################################################################
# Function: main
# Description: 
# Parameters: N/A
# Return values: desired program output
# Pre-Conditions:
# Post-Conditions:
#######################################################################

def main():
    
    # Get user input in order customers, servers, shift time
    inputData = get_input()

    # Assign each customer a service
    serviceData = assign_service(inputData)

    # Assign each customer a time
    serviceData = service_time(serviceData)

    # Set up list of server data
    serverData = []
    for i in range(inputData[1]):
        serverData.append([i, 0])

    allData = server_utilization(serviceData, serverData, inputData[2])

    # Print results
    print(" Customer ID ")
    for i in range(68):
        print("-", end="")

    




main()