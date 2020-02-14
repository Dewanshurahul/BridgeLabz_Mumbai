#Printing The Successive Element of Power of 2 According to Given Integer Value (number)
number = int(input("Enter any Number: "))
driverVariable = 1;
while driverVariable <= number:
    print(pow(2,driverVariable))
    driverVariable+=1