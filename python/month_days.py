#printing days in a month by month number

def month_days(month):
    if month == 1:
        print("January with 31 days")
    elif month == 2:
        print("February with 28 days")
    elif month == 3:
        print("March with 31 days")
    elif month == 4:
        print("Arpil with 30 days")
    elif month == 5:
        print("May with 31 days")
    elif month == 6:
        print("June with 30 days")
    elif month == 7:
        print("July with 31 days")
    elif month == 8:
            print("August with 31 days")
    elif month == 9:
            print("September with 30 days")
    elif month == 10:
            print("October with 31 days")
    elif month == 11:
            print("November with 30 days")
    elif month == 12:
            print("December with 31 days")
    else:
        print("Invalid month number")


month = int(input("Enter month number (1-12): "))
month_days(month)