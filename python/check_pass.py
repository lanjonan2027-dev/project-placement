def check_password(password):
    has_digit = False

    for ch in password:
        if ch.isdigit():
            has_digit = True
            break

    if len(password) >= 8 and has_digit:
        print("Valid password")
    else:
        print("Invalid password")


password = input("Enter password: ")
check_password(password)