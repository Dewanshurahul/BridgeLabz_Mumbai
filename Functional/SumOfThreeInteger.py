#Printing the Element of List who's combination makes a Sum of Zero('0')
size = int(input("Enter the number of element"))
numbers = []
for counter in range(size):
    numbers.append(int(input("Enter " + str(counter + 1) + " Element")))
for i in range(size - 2):
    for j in range(i+1, size - 1):
        for k in range(j+1, size):
            if (numbers[i] + numbers[j] + numbers[k]) == 0:
                print(str(numbers[i]) + " " + str(numbers[j]) + " " + str(numbers[k]))