#Take an alphabet and check if it lies between a and m or n and z

def alphabet(char):
    if 'a' <= char <= 'm':
        print("Alphabet lies between 'a' and 'm' ")
    elif 'n' <= char <= 'z':
        print("Alphabet lies between 'n' and 'z' ")
    else:
        print("Invalid character")

char = input("enter the alphabet").lower()
alphabet(char)