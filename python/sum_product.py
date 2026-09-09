def check_sum_product(num):
    sum_digits = 0
    product_digits = 1

    while num > 0:
        digit = num % 10
        sum_digits = sum_digits + digit
        product_digits = product_digits * digit
        num = num // 10

    if sum_digits > product_digits:
        print("Sum of digits is greater than product.")
    else:
        print("Sum of digits is not greater than product.")


num = int(input("Enter an integer (1-9999): "))

if num >= 1 and num <= 9999:
    check_sum_product(num)
else:
    print("Invalid input.")