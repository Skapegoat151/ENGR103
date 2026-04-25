
#Get input
scrap1 = float(input("What is the Scrap Percentage for Step 1? Enter it as a number between 0 and 1: "))
scrap2 = float(input("What is the Scrap Percentage for Step 2? Enter it as a number between 0 and 1: "))
scrap3 = float(input("What is the Scrap Percentage for Step 3? Enter it as a number between 0 and 1: "))
wReq = int((float(input("What is the number of good widgets required as output for step 3 per shift?: ")) // 1) + 1)
partTime = float(input("What is the standard time per part (in hours)?: "))
shiftTime = float(input("What is the number of hours per shift (in hours)?: "))
reliability = float(input("What is the machine reliability percentange? Enter it as a number between 0 and 1: "))
efficiency = float(input("What is the machine efficiency percentange? Enter it as a number between 0 and 1: "))

#Do calculations
scrapSum = (1-scrap1) * (1-scrap2) * (1-scrap3)
totalWidget = wReq / scrapSum
machineReq = (partTime * totalWidget) / (shiftTime * reliability * efficiency)

#Print results
print(round(machineReq, 2))
print(int(round(machineReq, 0)))