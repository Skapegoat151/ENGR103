import sys

'''def check_input_mag(input_num):
    # If number < 10 print "Too small!"
    if input_num < 10:
        print("Too small")
    #Else if number > 10 print "Too large"
    elif input_num > 10:
        print("Too large")
    #Else print Error check ID - show you get here with 10 entered
    else:
        #Sometimes you may want to add an error message
        #for unexpected location/action in your code.
        print("Error check ID")
    
def main():
    try:
        user_input_num = float(input("enter a number: "))
    except:
        print("Input error, try again!")
        sys.exit()
    
    check_input_mag(user_input_num)

main()
'''

'''
get ozone levels
check if ozone level entry is an integer
if <= 50 then rating = good
else if 51-100 then ratio = moderate
else if 101-150 then ratio = unhealthy (for sensitive groups)
else if 151-200 then ratio = unhealthy
else if 201-300 then ratio = very unhealthy
else if 301-500 then ratio = hazardous
'''

def num_checker(num):
    while isinstance(num, str):
        try:
            num = float(num)
        except:
            print("Please only enter numbers")
            num = input("Enter the current ozone level: ")

    return float(num)

def main():
    ozone = input("Enter the current ozone level: ")

    ozone = num_checker(ozone)
    
    while ozone > 500 or ozone < 0:
        print("Please only enter numbers from 0 - 500")
        ozone = input("Enter the current ozone level: ")
        ozone = num_checker(ozone)

    if ozone <= 50:
        print("Ozone Ratio: Good")
    elif ozone <= 100:
        print("Ozone Ratio: Moderate")
    elif ozone <= 150:
        print("Ozone Ratio: Unhealthy (for sensitive groups)")
    elif ozone <= 200:
        print("Ozone Ratio: Unhealthy")
    elif ozone <= 300:
        print("Ozone Ratio: Very Unhealthy")
    elif ozone <= 500:
        print("Ozone Ratio: Hazardous")

main()