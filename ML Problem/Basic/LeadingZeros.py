class LeadingZeros:
    def addLeadingZeros(self,string,size):
        for num in range(size):
            string = "0"+ string
        return string

l = LeadingZeros()
print(l.addLeadingZeros('dewanshu',2))