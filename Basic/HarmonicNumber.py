number = int(input("Enter number to find Harmonic Value: "))
harmonicNumber = 0
driverVariable = 1
while driverVariable <= number:
    harmonicNumber += 1 / driverVariable
    driverVariable+=1
print(harmonicNumber)