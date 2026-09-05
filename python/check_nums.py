def check_numbers(a, b):
    if a > 0 and b > 0 and (a + b) < 100:
        print("Condition satisfied")
    else:
        print("Condition not satisfied")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

check_numbers(a, b)