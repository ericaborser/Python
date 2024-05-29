#Distance between Two Points
from math import sqrt

print("\t\t\tDistance between Two Points")
x1=eval(input("Type the Value of X1: "))
x2=eval(input("Type the Value of X2: "))
y1=eval(input("Type the Value of Y1: "))
y2=eval(input("Type the Value of Y2: "))

distance=sqrt(((x2-x1)**2)+((y2-y1)**2))

print("The distance of the two points is ",distance,".",sep="")
print("The distance of the two points is ",round(distance,2),".",sep="")