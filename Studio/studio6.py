'''
for each day
    get number of classes
    for each class
        get length
'''

def userHours():
    check = True
    while check == True:
        hours = input("Hours: ")
        try:
            hours = int(hours)
            if hours < 0:
                print("Please only input numbers greater than 0")
            else:
                check = False
        except:
            print("Please only input whole numbers")
    
    return hours

def userMinutes():
    check = True
    while check == True:
        minutes = input("Minutes: ")
        try:
            minutes = int(minutes)
            if minutes < 0:
                print("Please only input numbers greater than 0")
            else:
                check = False
        except:
            print("Please only input whole numbers")
    
    return minutes

def userClasses(day):
    check = True
    while check == True:
        classes = input(f"Enter the number of classes you have on {day}: ")
        try:
            classes = int(classes)
            if classes < 0:
                print("Please only input numbers greater than 0")
            else:
                check = False
        except:
            print("Please only input whole numbers")

    return classes


def classTime(numClasses, day):
    hours = 0
    minutes = 0
    for i in range(1, numClasses+1):
        print("Enter the number of hours and the number of minutes for class", i, "on", day)
        hours += userHours()
        minutes += userMinutes()
    
    time = hours + (minutes/60)

    return time

def main():
    time1 = 0
    time2 = 0
    time3 = 0
    time4 = 0
    time5 = 0
    for i in range(1, 6):
        if i == 1:
            classes = userClasses("Monday")
            if classes == 0:
                continue
            else:
                time1 = classTime(classes, "Monday")
        
        elif i == 2:
            classes = userClasses("Tuesday")
            if classes == 0:
                continue
            else:
                time2 = classTime(classes, "Tuesday")

        elif i == 3:
            classes = userClasses("Wednesday")
            if classes == 0:
                continue
            else:
                time3 = classTime(classes, "Wenesday")

        elif i == 4:
            classes = userClasses("Thursday")
            if classes == 0:
                continue
            else:
                time4 = classTime(classes, "Thursday")

        elif i == 5:
            classes = userClasses("Friday")
            if classes == 0:
                continue
            else:
                time5 = classTime(classes, "Friday")

    print(f"You have {time1:.2f} hours of classes on Monday")
    print(f"You have {time2:.2f} hours of classes on Tuesday")
    print(f"You have {time3:.2f} hours of classes on Wednesday")
    print(f"You have {time4:.2f} hours of classes on Thursday")
    print(f"You have {time5:.2f} hours of classes on Friday")
            



main()