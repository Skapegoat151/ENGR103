
age = int(input("Enter your age: "))
height = int(input("Enter your height in inches: "))
ticket = (input("Do you have a ticket, Yes or No: ")).lower()

if ticket != "yes":
    print("No Entry.")
elif age >= 12 and height >= 54:
    print("Allowed on ride.")
else:
    print("Not allowed on ride.")