# lwap year

def leap_year(year):
    if year % 4 ==0 and year % 400 ==0:
        print("The year is a leap year.")
    elif year %100 != 0 and year % 4 ==0:
        print("The year is a leap year.")
    else:
        print("The year is not a leap year.")

leap_year(2023)

