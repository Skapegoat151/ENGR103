# print(20/2+4+5.5+3*4)
# print(20/(2+4+5.5)+2/4)
# print(20/2+4+5.5+2/4)
# print(25%5*6+12%36)
# print(25%5*(6+12)%36)
# print(2*(45.0+10)/3)
# print(2*45.0+10.0//12)
# print(2*45.0+10//12)
# print(2**8/(6+12)*2)

mpg = float(input("How many miles per gallon does your car get? "))
gal = 100000/mpg
lowGas = gal*2.5
highGas = gal*4.5
print("Gallons of gas: ", gal, "\nIf gas costs $2.50/gallon: ", lowGas, "\nIf gas costs $4.50/gallon: ", highGas)