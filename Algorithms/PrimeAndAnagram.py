class PrimeAndPalindrome:

    def palindrome(number):
        tempNumber = 0
        variable = number
        while number != 0:
            temp = number % 10
            tempNumber = 10 * tempNumber + temp
            number = number // 10
        return variable == tempNumber


    def prime(number):
        if number < 2:
            return False
        for num in range(2,number):
            if number % num == 0:
                return False
        else:
            return True



    for number in range(1001):
        if palindrome(number) and prime(number):
            print(number,end=" ")
