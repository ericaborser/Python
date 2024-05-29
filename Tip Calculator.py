#Tip Calculator

print("\n\t\t\tPROGRAM FOR NO.2")
print("\t\t\tTIP CALCULATOR")
price=eval(input("PRICE OF THE MEAL: "))
tip=eval(input("PERCENT TIP: "))

tipamount=(tip/100)*price
bill=tipamount+price

print("\nTIP AMOUNT: ",round(tipamount,2))
print("TOTAL BILL:",round(bill,2))
