def check_gp(a, b, c):
    if b * b == a * c:
        print("The numbers are in Geometric Progression.")
    else:
        print("The numbers are not in Geometric Progression.")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

check_gp(a, b, c)