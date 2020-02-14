from random import random
counter = 0
head = 0
numberOfFlips = int(input("Enter how many times you want to FLIP the coin: "))
while counter < numberOfFlips:
    flipValue = random()
    if flipValue >= 0.5:
        head += 1
    counter += 1
print(int(head / numberOfFlips*100))