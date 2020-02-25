def merge(listOfWord, low, high, mid):
    tempList = []
    i, j = low, mid + 1
    while i <= mid and j <= high:
        if str(listOfWord[i]) < str(listOfWord[j]):
            tempList.append(listOfWord[i])
            i += 1
        else:
            tempList.append(listOfWord[j])
            j += 1
    while i <= mid:
        tempList.append(listOfWord[i])
        i += 1
    while j <= high:
        tempList.append(listOfWord[j])
        j += 1
    for index in range(len(tempList)):
        listOfWord[index+low] = tempList[index]

def mergeSort(listOfWord, low, high):
    if low < high:
        mid = (low + high)//2
        mergeSort(listOfWord,low,mid)
        mergeSort(listOfWord,mid+1,high)
        merge(listOfWord,low,high,mid)


def binarySearch(word, listOfWord, low, high):
    if low > high:
        return False
    mid = (low+high) // 2
    if str(word) == str(listOfWord[mid]):
        return True
    elif str(word) > str(listOfWord[mid]):
        return binarySearch(word,listOfWord,mid+1,high)
    elif str(word) < str(listOfWord[mid]):
        return binarySearch(word,listOfWord,low,mid-1)


def bubbleSort(sequence):
    for index in range(len(sequence)):
        for ind in range(index+1,len(sequence)):
            if str(sequence[index]) > str(sequence[ind]):
                temp = sequence[index]
                sequence[index] = sequence[ind]
                sequence[ind] = temp

def insertionSort(listOfWord):
    for index in range(1,len(listOfWord)):
        tempIndex = index - 1
        temp = str(listOfWord[index])
        while tempIndex >= 0 and temp < str(listOfWord[tempIndex]):
            listOfWord[tempIndex + 1] = listOfWord[tempIndex]
            tempIndex -= 1
        listOfWord[tempIndex + 1] = temp


string = ["Dewanshu",5,"Nikhil","Dev","Nilesh"]
mergeSort(string, 0, len(string)-1)
print(binarySearch("Nilesh",string,0,len(string)-1))
print(string)