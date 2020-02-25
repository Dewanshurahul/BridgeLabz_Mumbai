class Prime:

    def prime(number):
        if number < 2:
            return False
        for num in range(2,number):
            if number % num == 0:
                return False
        else:
            return True


    for number in range(1001):
        if prime(number):
            print(number,end=" ")