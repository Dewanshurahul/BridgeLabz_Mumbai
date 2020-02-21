import operator
class Dictionary:

    # Return the sorted Dictionary based on values in Ascending Order
    # But Not Completely Working (Only Values are Sorted Not the Keys)

    # def sortAsc(self, dictionary):
    #     for index in list(dictionary):
    #         for ind in list(dictionary):
    #             if dictionary.get(index) < dictionary.get(ind):
    #                 t = dictionary.get(index)
    #                 dictionary[index] = dictionary.get(ind)
    #                 dictionary[ind] = t
    #     return dictionary

    # Return the sorted Dictionary based on values in Ascending Order
    def sortAsc(self,givenDictionary):
        return sorted(givenDictionary.items(),key=operator.itemgetter(1))

    # Add a key value pair to the existing dictionary
    def add(self,key,value,givenDictionary):
        givenDictionary[key] = value
        return givenDictionary

    # Concatinate all the passed dictionaries
    def concatinate(self, *args):
        requiredDictionary = {}
        for index in range(len(args)):
            for element in args[index]:
                requiredDictionary[element] = args[index].get(element)
        return requiredDictionary

    # Print each Key : Value Pair
    def show(self,givenDictionary):
        for element in givenDictionary:
            print(str(element),":",str(givenDictionary.get(element)))

    """
    Generate square of keys and pass as value by taking some integer as an argument 
    and set the limit for iteration
    and return the Dictionary
    e.g {1:1, 2:4, 3:9, 4:16 ...........}
    """
    def generatePowerDictionary(self,upto):
        requiredDictionary = {}
        for value in range(1,upto+1):
            requiredDictionary[value] = value*value
        return requiredDictionary

    # Remove the Element based on the passed key
    def remove(self,key,givenDictionary):
        requiredDictionary = {}
        for element in givenDictionary:
            if element == key:
                continue
            else:
                requiredDictionary[element] = givenDictionary.get(element)
        return requiredDictionary

    # Return the Unique Values from the the Dictionary in the form of List
    def uniqueValues(self,givenDictionary):
        tempList = []
        for keys in givenDictionary:
            tempList.append(givenDictionary.get(keys))
        return set(tempList)

    # Return a dictionary with the character as keys and there count as Values from the passed String
    def occurenceOfCharacter(self,givenString):
        requiredDictionary = {}
        for index in range(len(givenString)):
            count = 0
            for ind in range(index,len(givenString)):
                if givenString[index] == givenString[ind]:
                    count += 1
            if givenString[index] not in  requiredDictionary:
                requiredDictionary[givenString[index]] = count
        return requiredDictionary

    # Print the Passed Dictionary as Table
    def printTable(self,givenDictionary):
        for element in givenDictionary:
            print(element +" "+str(givenDictionary.get(element)))

    # Return the True Count value for a Key in Dictionary
    def countTrue(self,givenDictionary):
        count = 0
        for element in givenDictionary:
            if element == "success" and givenDictionary.get(element) =="True":
                count += 1
        return count

    # Take a list as an Argument and Return the Nested Dictionay of Keys
    # def nestedDictionary(self,listOfKeys):
    #     current = newDictionary = {}
    #     for keys in listOfKeys:
    #         newDictionary[keys] = {}
    #         newDictionary = newDictionary[keys]
    #     return current

    # Return True if Duplicate Keys are Present else Return False
    def multipleKeys(self,givenDictionary):
        for element in givenDictionary:
            flag = 0
            for ele in givenDictionary:
                if element == ele and flag == 1:
                    return False
                if element == ele and flag == 0:
                    flag = 1
        return True

    # Count the Number of list Present in the passed Dictionary as Value
    def countList(self,givenDictionary):
        count = 0
        for element in givenDictionary:
            if type(givenDictionary.get(element)) == list:
                count += 1
        return count


# Code For Testing the Above Written Codes(Functions)

d = Dictionary()
string = "DewDewanahe"
detail = {"name": 35, "age": 23}
lst = ["name","age","place","mind"]
#print(d.occurenceOfCharacter(string))
d.printTable(detail)