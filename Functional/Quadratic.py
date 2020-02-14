from math import sqrt

a = int(input("Enter the Value of a into an Equation: "))
b = int(input("Enter the Value of b into an Equation: "))
c = int(input("Enter the Value of c into an Equation: "))
delta = (b*b) - (4*a*c)
root1 = (-b + sqrt(delta/(2*a)))
root2 = (-b - sqrt(delta/(2*a)))
print("Root first: "+str(root1))
print("Root second: "+str(root2))