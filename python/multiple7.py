def check_number(num):
    if num % 7 == 0 or num % 10 == 7:
        return True
    else:
        return False

check_number(10)

if check_number(num):
    print("The number is a multiple of 7 or ends with 7")
else:
    print("The number is neither a multiple of 7 nor ends with 7")