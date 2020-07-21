import re

# Search Operation with match function
name = "Dewanshu Rahul"
searchPattern = input("Enter the Pattern to be searched : ")
x = re.search(searchPattern,name)
if x:
    print("Yes! Match found",x.span())
else:
    print("No! Match not found")

# Findall Function
y = re.findall("ewa",name)
print("Findall output: ",y)

# Sub Function
# Replaces the match with specified Text
z = re.sub("\s","_",name)
print("Sub function output: ",z)

# Split Function
m = re.split("\s",name)
print("Split function output: ",m)

