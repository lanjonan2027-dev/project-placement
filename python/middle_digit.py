num = int(input("Enter a 3-digit number: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

if b > a and b > c:
    print("Middle digit is the largest")
elif b < a and b < c:
    print("Middle digit is the smallest")
else:
    print("Middle digit is neither")