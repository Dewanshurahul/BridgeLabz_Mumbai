class List:

    def sum(self, lst):
        add = 0
        for index in range(len(lst)):
            add += lst[index]
        return add

    def mul(self, lst):
        if len(lst) == 0:
            return None
        multiply = 1
        for index in range(len(lst)):
            multiply *= lst[index]
        return multiply

    def min(self, lst):
        if len(lst) != 0:
            small = lst[0]
        else:
            return None
        for index in range(len(lst)):
            if small > lst[index]:
                small = lst[index]
        return small

    def lengthCondition(self, lst):
        if len(lst) == 0:
            return None
        count = 0
        for index in range(len(lst)):
            if len(lst[index]) > 1 and lst[index][0] == lst[index][-1]:
                count += 1
        return count

    def sortListByTuple(self, lst):
        if len(lst) == 0:
            return 'No Element To SORT'
        for index in range(len(lst)):
            for ind in range(index + 1, len(lst)):
                if lst[index][-1] > lst[ind][-1]:
                    t = lst[index]
                    lst[index] = lst[ind]
                    lst[ind] = t
        return lst

    def removeDuplicate(self, lst):
        return list(set(lst))

    def copy(self, listOfValues):
        newList = []
        for index in range(len(listOfValues)):
            newList.append(listOfValues[index])
        return newList

    def wordsOfSpecificLength(self, listOfWords, length):
        lst = []
        for index in range(len(listOfWords)):
            if len(listOfWords[index]) > length:
                lst.append(listOfWords[index])
        return lst

    def commonMember(self, firstList, secondList):
        for index in range(len(firstList)):
            for ind in range(len(secondList)):
                if firstList[index] == secondList[ind]:
                    return True
        return False

    def modifiedList(self, listOfElements):
        newList = []
        for index in range(len(listOfElements)):
            if index == 0 or index == 4 or index == 5:
                continue
            else:
                newList.append(listOfElements[index])
        return newList

    def differenceBetweenList(self,firstList,secondList):
        newList = []
        for index in range(len(secondList)):
            if secondList[index] not in firstList and secondList[index] not in newList:
                newList.append(secondList[index])
        for index in range(len(firstList)):
            if firstList[index] not in secondList and firstList[index] not in newList:
                newList.append(firstList[index])
        return newList

    def appendAnotherList(self, firstList, secondList):
        for index in range(len(secondList)):
            firstList.append(secondList[index])
        return firstList

    # def circularIdentical(self,firstList,secondList):
    #     pass

    def commonItems(self, firstList, secondList):
        lst = []
        for index in range(len(firstList)):
            for ind in range(len(secondList)):
                if firstList[index] == secondList[ind]:
                    lst.append(firstList[index])
        return list(set(lst))

    # def splitBasedOnFirstCharacter(self,givenList):
    #     pass

    # def removeDuplicateListOfList(self,givenList):
    #     pass




l = List()
lst = [10, 20, 40, 30, 56, 25, 10, 20, 33, 40]
lst1 = [10, 30, 56]
print(l.differenceBetweenList(lst,lst1))