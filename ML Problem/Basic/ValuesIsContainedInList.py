size = int(input("Enter Size Of List"))
lst = []
for index in range(size):
    data = input("Enter "+str(index+1)+" data: ")
    lst.append(data)
value = input("Enter the Value To be Searched.")
for index in range(size):
    if value == lst[index]:
        print(value+" is Found")
        break
else:
    print("Value is Not Found")