class List:

    # To add every element of passed List and return the Value
    def sum(listOfValues):
        add = 0
        for index in range(len(listOfValues)):
            add += lst[index]
        return add

    # Multiply every Element of List and return the value
    def mul(listOfElement):
        if len(listOfElement) == 0:
            return None
        multiply = 1
        for index in range(len(listOfElement)):
            multiply *= listOfElement[index]
        return multiply

    # Find the Minimum value among the List and reutn it.
    def min(listOfValues):
        if len(listOfValues) != 0:
            small = listOfValues[0]
        else:
            return None
        for index in range(len(listOfValues)):
            if small > listOfValues[index]:
                small = listOfValues[index]
        return small

    # Return the values from the passed List which have (length >= 2)
    # and First and Last Character are same
    def lengthCondition(listOfElement):
        if len(listOfElement) == 0:
            return None
        count = 0
        for index in range(len(listOfElement)):
            if len(listOfElement[index]) > 1 and listOfElement[index][0] == listOfElement[index][-1]:
                count += 1
        return count

    # Sort(ascending order) the List containing Tuple based on the last element of Tuple
    def sortListByTuple(listOfTuple):
        if len(listOfTuple) == 0:
            return 'No Element To SORT'
        for index in range(len(listOfTuple)):
            for ind in range(index + 1, len(listOfTuple)):
                if listOfTuple[index][-1] > listOfTuple[ind][-1]:
                    t = listOfTuple[index]
                    listOfTuple[index] = listOfTuple[ind]
                    listOfTuple[ind] = t
        return listOfTuple

    # Remove duplicate from the List
    def removeDuplicate(listOfValues):
        return list(set(listOfValues))

    # Copy the passed List and return a new List
    def copy(listOfValues):
        newList = []
        for index in range(len(listOfValues)):
            newList.append(listOfValues[index])
        return newList

    # Return the List of word which have length greater than passed in the Function
    def wordsOfSpecificLength(listOfWords, length):
        lst = []
        for index in range(len(listOfWords)):
            if len(listOfWords[index]) > length:
                lst.append(listOfWords[index])
        return lst

    # Take two List as an Argument and return True if they have atleast ONE element in common
    def commonMember(firstList, secondList):
        for index in range(len(firstList)):
            for ind in range(len(secondList)):
                if firstList[index] == secondList[ind]:
                    return True
        return False

    # Return the list ofter removing 0th,4th and 5th Element if Present
    def modifiedList(listOfElements):
        newList = []
        for index in range(len(listOfElements)):
            if index == 0 or index == 4 or index == 5:
                continue
            else:
                newList.append(listOfElements[index])
        return newList

    # Returning the List which contains unique elements from both the passed List
    def differenceBetweenList(firstList,secondList):
        newList = []
        for index in range(len(secondList)):
            if secondList[index] not in firstList and secondList[index] not in newList:
                newList.append(secondList[index])
        for index in range(len(firstList)):
            if firstList[index] not in secondList and firstList[index] not in newList:
                newList.append(firstList[index])
        return newList

    # Add the element of First List into other and return the Appended list
    def appendAnotherList(firstList, secondList):
        for index in range(len(secondList)):
            firstList.append(secondList[index])
        return firstList


    # def circularIdentical(firstList,secondList):
    #     pass

    # Return the List which contains common element(s)
    def commonItems(firstList, secondList):
        lst = []
        for index in range(len(firstList)):
            for ind in range(len(secondList)):
                if firstList[index] == secondList[ind]:
                    lst.append(firstList[index])
        return list(set(lst))


    # def splitBasedOnFirstCharacter(givenList):
    #     pass


    # def removeDuplicateListOfList(givenList):
    #     pass




firstList = ['101', '20', '40', '30', '56', '25', '10', '20', '33', '40']
emptyList = [(2,5), (5,1)]
lst1 = [10, 30, 56]
print(List.sortListByTuple(emptyList))