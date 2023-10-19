# This code tells you if the bank is open or not on the date you entered.
# The Bank is open from 10am to 9pm on weekdays




opening_hour = 10
closing_hour = 21


while True:
    day = int(input("Enter the day of the week (1 for Monday, 2 for Tuesday, etc.): "))
    hour = int(input("Enter the hour (00-23): "))
    if 1 <= day <= 7 and 0 <= hour <= 23:
        if day == 6 or day == 7:
            print("Closed")
            break
        elif opening_hour <= hour < closing_hour:
            print("Open")
            break
        else:
            print("Closed")
            break
    else:
        print("Invalid day or hour input.")






