def check_ap(a, b, c):
    if b - a == c - b:
        print("The numbers are in Arithmetic Progression.")
    else:
        print("The numbers are not in Arithmetic Progression.")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

check_ap(a, b, c)