#Creating a 2-D dynamic Array and Printing it's Elememt
rows = int(input("Enter ROW: "))
columns = int(input("Enter COLUMN: "))
#An Array of row * Columns is being created
myArray = [[ 0 for i in range(columns)] for j in range(rows)]
print(myArray)
for row in range(rows):
    for column in range(columns):
        #Assigning the User defined values to the Array
        myArray[row][column] = input("Enter")
print(myArray)
#Printing the Array Element-Wise
for row in range(rows):
    for column in range(columns):
        print(myArray[row][column])