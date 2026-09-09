def check_date(day, month):
    if month < 1 or month > 12:
        print("Invalid date.")
        return

    if month == 2:
        max_days = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        max_days = 30
    else:
        max_days = 31

    if day >= 1 and day <= max_days:
        print("Valid date.")
    else:
        print("Invalid date.")


day = int(input("Enter day: "))
month = int(input("Enter month: "))

check_date(day, month)