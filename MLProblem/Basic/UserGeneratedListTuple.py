size = int(input("Enter size of List and Tuple"))
userList = []
for index in range(size):
    data = input("Enter any Element")
    userList.append(data)
userTuple = tuple(userList)
print(userList)
print(userTuple)