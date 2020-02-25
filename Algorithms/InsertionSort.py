def insertionSort(listOfWord):
    for index in range(1,len(listOfWord)):
        tempIndex = index - 1
        temp = listOfWord[index]
        while tempIndex >= 0 and temp < listOfWord[tempIndex]:
            listOfWord[tempIndex + 1] = listOfWord[tempIndex]
            tempIndex -= 1
        listOfWord[tempIndex + 1] = temp




listOfString = ["Nikhil","Raman","Rahul","Dewanshu"]
print(listOfString)
insertionSort(listOfString)
print(listOfString)