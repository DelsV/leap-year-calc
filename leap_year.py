year = input("Which year would you like to check?")

leap_year = None

if year % 4 == 0:
    if year % 100 > 0:
        leap_year = True
    else:
        if year % 400 = 0:
            leap_year = True
        else:
            leap_year = False
else:
    leap_year = False

if leap_year:
    print("Leap year!")
else:
    print("NOT leap year!")