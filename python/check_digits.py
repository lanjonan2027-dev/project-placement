num = int(input("Enter an integer: "))

if -9 <= num <= 9:
    print("Single-digit number")
elif -99 <= num <= 99:
    print("Double-digit number")
else:
    print("Multi-digit number")