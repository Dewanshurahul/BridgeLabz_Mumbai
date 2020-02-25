class Tuple:

    # To print Every Element of passed Tuple
    # def show(tupleOfElements):
    #     for element in tupleOfElements:
    #         print(element,end=" ")
    #     print()

    # To create and return a empty Tuple
    def createTuple():
        return ()

    # Accepts the data to create and return a tuple
    def create(*args):
        return args

    # Copy and return a new Tuple from the passed Tuple
    def clone(givenTuple):
        return tuple(element for element in givenTuple)

    # Unpack a Tuple in different Variale
    # For that the Number of varable must be
    # equal to the Number of element in the Tuple
    newTuple = ("Dewanshu", "Rahul", 23)
    firstName, lastName, age = newTuple
    print(firstName, lastName, age)

    # Return repeated item(s) inside a tuple
    def repeatedItem(givenTuple):
        tempList = []
        for index in range(len(givenTuple)):
            for ind in range(index + 1, len(givenTuple)):
                if givenTuple[index] == givenTuple[ind]:
                    tempList.append(givenTuple[index])
        return tuple(tempList)

    # Return True if passed element is present in Tuple or
    # Return False if passes element is not present in Tuple
    def exists(element, givenTuple):
        return element in givenTuple

    # Takes a Sequence as an input and return back a Tuple
    def convertToTuple(listOfItems):
        return tuple(element for element in listOfItems)

    # Remove a particular element from the Tuple
    def remove(ele, tupleOfElement):
        tempList = []
        for element in tupleOfElement:
            if element != ele:
                tempList.append(element)
        return tuple(tempList)

    # Slice a tuple based on passed index
    def slice(firstIndex, lastIndex, givenTuple):
        return tuple(list(givenTuple)[firstIndex:lastIndex])

    # Reverse the passed Tuple
    def reverse(givenTuple):
        return tuple(reversed(givenTuple))


tup = ("Dewanshu", "Rahul", 23, "Dewanshu", 23)
print(Tuple.repeatedItem(tup))