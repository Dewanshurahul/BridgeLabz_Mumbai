#Taking the co-ordinated from thw Person and returning back it's EUCLIDEAN Distance
#importing square_root function from math class
from math import sqrt
x_axis = int(input("Enter the distance in X-Axis"))
y_axis = int(input("Enter the distance in Y-Axis"))
distance = sqrt(pow(x_axis,2) + pow(y_axis, 2))
print(distance)