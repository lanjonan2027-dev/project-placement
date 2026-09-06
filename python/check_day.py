def check_day(day):
    if day >= 1 and day <= 5:
        print("Weekday")
    elif day == 6 or day == 7:
        print("Weekend")
    else:
        print("Invalid day")


day = int(input("Enter weekday number (1-7): "))
check_day(day)