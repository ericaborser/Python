#Write a program that asks the user to enter two numbers, 
#x and y, and computes (|𝒙−𝒚|)/(𝒙+𝒚)

x=eval(input("X: "))
y=eval(input("Y: "))
diff= x-y
sum= x+y
print("x-y=", diff)
print("x+y=", sum)
print("Answer: ", diff/sum)

#rounding off
print("Answer: ", round(diff/sum,2))


