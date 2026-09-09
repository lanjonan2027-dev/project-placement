def find_century(year):
    century = (year - 1) // 100 + 1

    if century % 10 == 1 and century != 11:
        suffix = "st"
    elif century % 10 == 2 and century != 12:
        suffix = "nd"
    elif century % 10 == 3 and century != 13:
        suffix = "rd"
    else:
        suffix = "th"

    print(century, suffix, "century")


year = int(input("Enter year: "))

if year > 0:
    find_century(year)
else:
    print("Invalid year.")