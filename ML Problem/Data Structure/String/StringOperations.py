class String:

    def length(self, givenString):
        return len(givenString)

    def characterOccurence(self, givenString):
        character = {}
        for char in range(len(givenString)):
            count = 0
            for charac in range(char, len(givenString)):
                if givenString[char] == givenString[charac]:
                    count += 1
            if givenString[char] not in character:
                character[givenString[char]] = count
        return character

    def changeFirstCharacterOccurence(self, givenString):
        target = givenString[0]
        newstring = target
        for index in range(1, len(givenString)):
            if givenString[index] == target:
                newstring += '$'
            else:
                newstring += givenString[index]
        return newstring

    def addSuffix(self, givenString):
        if len(givenString) < 3:
            return givenString
        if givenString[-3:] != 'ing':
            return givenString + 'ing'
        else:
            return givenString + 'ly'

    def longestWord(self, listOfWord):
        large = len(listOfWord[0])
        for index in range(len(listOfWord)):
            if large < len(listOfWord[index]):
                large = len(listOfWord[index])
        return large

    def lowerAndUpper(self, givenString):
        return givenString.upper(), givenString.lower()

    def uniqueSorted(self, sequenceOfWord):
        listOfWord = list(set(sequenceOfWord))
        for index in range(len(listOfWord)):
            for ind in range(index, len(listOfWord)):
                if listOfWord[index] > listOfWord[ind]:
                    temp = listOfWord[index]
                    listOfWord[index] = listOfWord[ind]
                    listOfWord[ind] = temp
        return listOfWord

    def lastPart(self, character, givenString):
        if character not in givenString:
            return None
        index = -1
        for ind in range(len(givenString)):
            if character == givenString[ind]:
                index = ind
        return givenString[index:]

    def occurenceSub_String(self, subStr, givenString):
        count = 0
        for index in range(len(givenString)):
            if subStr == givenString[index:index + len(subStr)]:
                count += 1
        return count

    def reverse(self, givenString):
        revString = ""
        for index in range(len(givenString)):
            revString = givenString[index] + revString
        return revString

    def lowerFirstNCharacter(self, n, givenString):
        return givenString[:n].lower() + givenString[n:]


s = String()
# string = ["zdew","fdedwa","dewanshu","nikhil","zdew"]
string = "RAHUL"
print(s.lowerFirstNCharacter(3, string))
