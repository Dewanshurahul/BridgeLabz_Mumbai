class Anonymous:
    def numberMod15(self,lst):
        return list(filter(lambda n : n%15==0,lst))




a = Anonymous()
size = int(input("Enter Size of List"))
lst = []
for index in range(size):
    data = int(input("Enter Only Number"))
    lst.append(data)
print(a.numberMod15(lst))