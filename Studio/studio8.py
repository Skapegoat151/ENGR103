# Studio 6 but with 2D lists

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
    time = []
    hours = 0
    minutes = 0
    for i in range(1, numClasses+1):
        print("Enter the number of hours and the number of minutes for class", i, "on", day)
        hours = userHours()
        minutes = userMinutes()
        time.append(hours + (minutes/60))

    return time

def main():
    
    times = []
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    for i in range(1, 6):
        if i == 1:
            classes = userClasses("Monday")
            if classes == 0:
                times.append(0)
            else:
                times.append(classTime(classes, "Monday"))
        
        elif i == 2:
            classes = userClasses("Tuesday")
            if classes == 0:
                times.append(0)
            else:
                times.append(classTime(classes, "Tuesday"))

        elif i == 3:
            classes = userClasses("Wednesday")
            if classes == 0:
                times.append(0)
            else:
                times.append(classTime(classes, "Wenesday"))

        elif i == 4:
            classes = userClasses("Thursday")
            if classes == 0:
                times.append(0)
            else:
                times.append(classTime(classes, "Thursday"))

        elif i == 5:
            classes = userClasses("Friday")
            if classes == 0:
                times.append(0)
            else:
                times.append(classTime(classes, "Friday"))

    for i in range(5):
        if times[i] == 0:
            print("\nYou do not have class on", days[i], end = " ")
        else:
            formatList = []
            for j in range(len(times[i])):
                formatList.append(f"{times[i][j]:.2f}")
            print(f"\nYou have {sum(times[i]):.2f} hours of classes on {days[i]}, broken up into", end = " ")
            for j in range(len(formatList)):
                print(formatList[j], end = " ")
            

main()