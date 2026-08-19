num = int(input("Enter a 4-digit number: "))

first = num // 1000
last = num % 10

if first == last:
    print("First and last digits are equal")
else:
    print("First and last digits are not equal")