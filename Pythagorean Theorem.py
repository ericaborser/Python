#Pythagorean Theorem

from math import sqrt
print("\nPythagorean Theorem")
a=eval(input("Type the value of A: "))
c=eval(input("Type the value of C: "))

b=sqrt((c**2)-(a**2))
print("The value of B is ",b,".",sep="")
print("The value of B is ",round(b),".",sep="")
