def merge(listOfWord, low, high, mid):
    tempList = []
    i, j = low, mid + 1
    while i <= mid and j <= high:
        if listOfWord[i] < listOfWord[j]:
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


listOfString = ["Nikhil","Raman","Rahul","Dewanshu"]
print(listOfString)
mergeSort(listOfString, 0, len(listOfString)-1)
print(listOfString)