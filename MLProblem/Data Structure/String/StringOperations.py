class String:

    # Return the length of the passed String
    def length(givenString):
        return len(givenString)

    # Return the dictionary containing the occurence of character of passed String
    def characterOccurence(givenString):
        character = {}
        for char in range(len(givenString)):
            count = 0
            for charac in range(char, len(givenString)):
                if givenString[char] == givenString[charac]:
                    count += 1
            if givenString[char] not in character:
                character[givenString[char]] = count
        return character

    # Change the occurence of first character of the String except the First Character
    def changeFirstCharacterOccurence(givenString):
        target = givenString[0]
        newstring = target
        for index in range(1, len(givenString)):
            if givenString[index] == target:
                newstring += '$'
            else:
                newstring += givenString[index]
        return newstring


    # If the length of String is less than 3 return same string
    # Else if the string is not suffixed with 'ing' then return the string by adding 'ing' at the end
    # else if the string id suffixed with'ing' then return the string by adding 'ly' at the end
    def addSuffix(givenString):
        if len(givenString) < 3:
            return givenString
        if givenString[-3:] != 'ing':
            return givenString + 'ing'
        else:
            return givenString + 'ly'

    # Return the length of word which have largest Length in the List
    def longestWord(listOfWord):
        large = len(listOfWord[0])
        for index in range(len(listOfWord)):
            if large < len(listOfWord[index]):
                large = len(listOfWord[index])
        return large

    # Return the passed string in upper as well as in lower case
    def lowerAndUpper(givenString):
        return givenString.upper(), givenString.lower()

    # Return the UNIQUE sequence of word in sorted form (alphaNumerically)
    def uniqueSorted(sequenceOfWord):
        listOfWord = list(set(sequenceOfWord))
        for index in range(len(listOfWord)):
            for ind in range(index, len(listOfWord)):
                if listOfWord[index] > listOfWord[ind]:
                    temp = listOfWord[index]
                    listOfWord[index] = listOfWord[ind]
                    listOfWord[ind] = temp
        return listOfWord

    # Return the last part of the string based on the passed Character
    def lastPart(character, givenString):
        if character not in givenString:
            return None
        index = -1
        for ind in range(len(givenString)):
            if character == givenString[ind]:
                index = ind
        return givenString[index:]

    # Rerturn the occurence of Sub-String in the given String
    def occurenceSub_String(subStr, givenString):
        count = 0
        for index in range(len(givenString)):
            if subStr == givenString[index:index + len(subStr)]:
                count += 1
        return count

    # Reverse the String
    def reverse(givenString):
        revString = ""
        for index in range(len(givenString)):
            revString = givenString[index] + revString
        return revString

    # Return the passed String after converting first N index into LowerCase based on passed index
    def lowerFirstNCharacter(upto, givenString):
        return givenString[:upto].lower() + givenString[upto:]


# string = ["zdew","fdedwa","dewanshu","nikhil","zdew"]
string = "RAHUL"
print(String.lowerFirstNCharacter(3, string))