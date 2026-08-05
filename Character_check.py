#Charcter check whether its uppercase, lowercase, digit or special character

def char_check(char):
    if char.isupper():
        print("Uppercase letter")
    elif char.islower():
        print("Lowercase letter")
    elif char.isdigit():
        print("Digit")
    else:
        print("Special character")

char_check('A')