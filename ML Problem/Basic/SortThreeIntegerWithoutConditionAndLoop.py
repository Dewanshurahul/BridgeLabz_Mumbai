a = int(input("Enter 1st Numbers"))
b = int(input("Enter 2nd Numbers"))
c = int(input("Enter 3rd Numbers"))
maxValue = max(a, b, c)
minValue = min(a, b, c)
print(str(minValue)+" "+str((a+b+c)-minValue-maxValue)+" "+str(maxValue))