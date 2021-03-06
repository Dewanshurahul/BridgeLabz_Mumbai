class Sets:

    #Return the Empty Set
    def createSet():
        return set({})

    # Print every element of the passed Set
    def show(setOfElements):
        for values in setOfElements:
            print(values, end=" ")
        print()

    # Add the passed element into the Given Set
    def addElement(element, setOfElement):
        setOfElement.add(element)
        return setOfElement

    # Take element(s) and remove from the passed Set if Present
    def removeItems(setOfElement, *element):
        for index in range(len(element)):
            if element[index] in setOfElement:
                setOfElement.remove(element[index])
        return setOfElement

    # Take one element and remove it from the Set if Present
    def removeMember(element, setOfElement):
        if element in setOfElement:
            setOfElement.remove(element)
        return setOfElement

    # Return the element which are common in both the Set
    def intersectionOfSets(firstSet, secondSet):
        intersectionSet = set({})
        for firstvalues in firstSet:
            for secondvalues in secondSet:
                if firstvalues == secondvalues:
                    intersectionSet.add(firstvalues)
        return intersectionSet

    # Return the elemets of both the Sets **UNION(Mathematical)**
    def unionOfSets(firstSet, secondSet):
        unionSet = set({})
        for values in firstSet:
            unionSet.add(values)
        for values in secondSet:
            unionSet.add(values)
        return unionSet

    # Return a new set with elements in the set that are not in the others
    def setDifference(firstSet,secondSet):
        differenceSet = set({})
        for firstValues in secondSet:
            for secondValues in firstSet:
                if firstValues == secondValues:
                    break
            else:
                differenceSet.add(firstValues)
        return differenceSet


    def symmetricDifference(firstSet,secondSet):
        differenceSet = set({})
        for firstValue in secondSet:
            for secondValue in firstSet:
                if firstValue == secondValue:
                    break
            else:
                differenceSet.add(firstValue)
        for firstValue in firstSet:
            for secondValue in secondSet:
                if firstValue == secondValue:
                    break
            else:
                differenceSet.add(firstValue)
        return differenceSet


    # def frozenSet(self):
    #     pass


    # Empty the passed Set
    def clear(setOfElement):
        while len(setOfElement) != 0:
            setOfElement.pop()
        return setOfElement

    # Return the minimum element of the Array
    def min(setOfElement):
        if len(setOfElement) != 0:
            minimum = setOfElement.pop()
            setOfElement.add(minimum)
        else:
            return None
        for values in setOfElement:
            if minimum > values:
                minimum = values
        return minimum

    # Return the Maximum element of the Array
    def max(setOfElement):
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
print(Sets.symmetricDifference(sets,secondSet))