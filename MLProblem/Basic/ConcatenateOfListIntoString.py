size = int(input("Enter size Of List"))
lst = []
for index in range(size):
    data = input("Enter "+str(index+1)+" data")
    lst.append(data)
string = ""
for index in range(size):
    string += lst[index]
print(string)