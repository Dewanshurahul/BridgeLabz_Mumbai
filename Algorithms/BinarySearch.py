def binarySearch(word, listOfWord, low,high):
    if low > high:
        return False
    mid = (low+high)//2
    if word == listOfWord[mid]:
        return True
    elif word > listOfWord[mid]:
        return binarySearch(word,listOfWord,mid+1,high)
    elif word < listOfWord[mid]:
        return binarySearch(word,listOfWord,low,mid-1)

givenList = []
size = int(input("Enter how many elements you want to Enter: "))
for index in range(size):
    data = input("Enter word: ")
    givenList.append(data)
target = input("Enter the Element To be searched.")
if binarySearch(target,givenList,0,len(givenList)):
    print(target+" is Present in The List")
else:
    print("Element is not present in the List")