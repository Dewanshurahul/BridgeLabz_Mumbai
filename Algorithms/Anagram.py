class Anagram:

    def anagram(firstString, secondString):
        if len(firstString) != len(secondString):
            return False
        checkList = []
        for char in range(len(firstString)):
            checkList.append(firstString[char])
        for char in range(len(secondString)):
            if secondString[char] in checkList:
                checkList.remove(secondString[char])
        return len(checkList) == 0


    string = "peek"
    string1 = 'keek'
    print(anagram(string,string1))