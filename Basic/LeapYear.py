# Checking Provided Year is a Leap Year or not a Leap Year
year = int(input("Enter Year: "))
if year > 999 and year < 10000:
    if year % 4 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(str(year) + " is Leap Year.")
    else:
        print(str(year) + " is not Leap Year")
else:
    print("Only Provide Year with 4 digits")
