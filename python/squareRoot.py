def root(number):
    if number < 0:
        return False
    else:
        i = 0

        while i * i <= number:
            if i * i == number:
                return True
            i += 1

        return False

number  = int(input("Enter: "))

if root(number):
    print ("Number is perfect square root")

else:
    print("Number is not a square root")