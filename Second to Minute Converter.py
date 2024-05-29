#Write a program that asks the user for a number of seconds 
#and print out how many minutes and seconds

sec=eval(input("How many second you want to convert: "))
min=sec//60
second=sec%60
print("There are ",min, " minutes and ", second, " seconds. ")
