def check_digits(num):
    first = num // 100
    middle = (num // 10) % 10
    last = num % 10

    if first + last == middle:
        print("Condition satisfied.")
    else:
        print("Condition not satisfied.")


num = int(input("Enter a 3-digit number: "))

if num >= 100 and num <= 999:
    check_digits(num)
else:
    print("Please enter a 3-digit number.")