user = eval(input('enter hour :'))
day = input('enter am (1) or pm (2) :')
hour = eval(input('How many hours ahead ?:'))


if day == 'pm' and user != 12:
    user += 12;
elif day == 'am' and user == 12:
    user = 0;

new_hour = user + hour;
new_hour = new_hour % 24;

    
if new_hour >= 0 and new_hour < 12:
    new_hour = new_hour % 12 ;
    if new_hour == 0:
        new_hour = 12;
    print(f'New hour : {new_hour}', end='am')
    print()
else:
    new_hour = new_hour % 12;
    if new_hour == 0:
        new_hour = 12 ;
    print(f'New hour : {new_hour}', end='pm')
    print()
    
    

