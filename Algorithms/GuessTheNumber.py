import random

number = int(input("Choose the number for range."))
def binarySearch(counter, randomNumber, low, high):
    if counter == nosOfQues:
        print('No chance remaining')
        return
    guessNumber = int(input("Enter the Number to guess the Random Number"))
    if guessNumber == randomNumber:
        print('Guess is Correct')
        return
    else:
        if randomNumber >= low and randomNumber <= high:
            print("Number is Between Range.")
        else:
            print('Number Out of Range.')
            return
    if randomNumber < guessNumber:
        print("Random number is Less than your input")
        return binarySearch(counter + 1, randomNumber, low, guessNumber)
    else:
        print("Random Number is Greater than your input.")
        return binarySearch(counter + 1, randomNumber, guessNumber, high)

def numberOfQuestions(number):
    countQuestion = 0
    tempValriable = number
    while tempValriable != 0:
        countQuestion += 1
        tempValriable //= 2
    return countQuestion - 1

def lengthOfDigit(number):
    length = 0
    temp = number
    while temp != 0:
        temp //= 10
        length += 1
    return length

def numberOftens(number):
    length = lengthOfDigit(number)
    tens = 1
    while length != 0:
        tens *= 10
        length -= 1
    return tens

randomNumber = ((random.random() * numberOftens(number) * 10) // 10) % number
print(randomNumber)
nosOfQues = numberOfQuestions(number)
binarySearch(0, randomNumber, 0, number)