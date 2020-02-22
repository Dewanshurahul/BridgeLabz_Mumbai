class Occurance:
    def characterOccurance(self,char,string):
        charCount = 0
        for index in range(len(string)):
            if char.lower() == string[index].lower():
                charCount += 1
        return charCount

o = Occurance()
print(o.characterOccurance('r', 'Rarul'))