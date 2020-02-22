from random import random

size = int(input("Enter the Number of Unique Copons You Want: "))
listOfRandom = []
count = 0
while True:
    number = (random()*100) // 10
    count += 1
    if number not in listOfRandom:
        listOfRandom.append(number)
    if len(listOfRandom) == size:
        break
print(count)
print(listOfRandom)