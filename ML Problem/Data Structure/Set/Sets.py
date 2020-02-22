class Sets:

    def createSet(self):
        newSet =set({})
        return newSet

    def show(self, setOfElements):
        for values in setOfElements:
            print(values, end=" ")
        print()

    def addElement(self, element, setOfElement):
        setOfElement.add(element)
        return setOfElement

    def removeItems(self, setOfElement, *element):
        for index in range(len(element)):
            if element[index] in setOfElement:
                setOfElement.remove(element[index])
        return setOfElement

    def removeMember(self, element, setOfElement):
        if element in setOfElement:
            setOfElement.remove(element)
        return setOfElement

    def intersectionOfSets(self, firstSet, secondSet):
        intersectionSet = set({})
        for firstvalues in firstSet:
            for secondvalues in secondSet:
                if firstvalues == secondvalues:
                    intersectionSet.add(firstvalues)
        return intersectionSet

    def unionOfSets(self, firstSet, secondSet):
        unionSet = set({})
        for values in firstSet:
            unionSet.add(values)
        for values in secondSet:
            unionSet.add(values)
        return unionSet

    def setDifference(self,firstSet,secondSet):
        differenceSet = set({})
        for firstValues in secondSet:
            for secondValues in firstSet:
                if firstValues == secondValues:
                    break
            else:
                differenceSet.add(firstValues)
        return differenceSet


    # def symmetricDifference(self,firstSet,secondSet):
    #     differenceSet = set({})
    #     for firstValues in secondSet:
    #         for secondValues in firstSet:
    #             if firstValues == secondValues:
    #                 break
    #         else:
    #             differenceSet.add(firstValues)
    #     return differenceSet


    # def frozenSet(self):
    #     pass


    def clear(self,setOfElement):
        while len(setOfElement) != 0:
            setOfElement.pop()
        return setOfElement

    def min(self, setOfElement):
        if len(setOfElement) != 0:
            minimum = setOfElement.pop()
            setOfElement.add(minimum)
        else:
            return None
        for values in setOfElement:
            if minimum > values:
                minimum = values
        return minimum

    def max(self, setOfElement):
        if len(setOfElement) != 0:
            maximum = setOfElement.pop()
            setOfElement.add(maximum)
        else:
            return None
        for values in setOfElement:
            if maximum < values:
                maximum = values
        return maximum




s = Sets()
sets = {7, 2, 5, 4, 6, 45}
secondSet = { 50,42,65,49,12,21,6,7,5 }
print(s.max(sets))