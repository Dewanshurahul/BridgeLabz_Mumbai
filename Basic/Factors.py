number = int(input("Enter any Number to find Prime Factors: "))
factor = 2
while int(number)!=0:
    if number % factor == 0:
        print(factor)
        number /= factor
    else:
        factor += 1