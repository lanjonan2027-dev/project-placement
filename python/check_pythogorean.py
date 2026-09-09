def check_pythagorean(a, b, c):
    if a >= b and a >= c:
        largest = a
        x = b
        y = c
    elif b >= a and b >= c:
        largest = b
        x = a
        y = c
    else:
        largest = c
        x = a
        y = b

    if x * x + y * y == largest * largest:
        print("They form a Pythagorean triplet.")
    else:
        print("They do not form a Pythagorean triplet.")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

check_pythagorean(a, b, c)