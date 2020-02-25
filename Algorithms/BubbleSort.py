def bubbleSort(sequence):
    for index in range(len(sequence)):
        for ind in range(index+1,len(sequence)):
            if sequence[index] > sequence[ind]:
                temp = sequence[index]
                sequence[index] = sequence[ind]
                sequence[ind] = temp


listOfInteger = [55,12,48,34,69]
print(listOfInteger)
bubbleSort(listOfInteger)
print(listOfInteger)