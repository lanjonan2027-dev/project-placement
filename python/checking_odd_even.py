#To check if both are odd, both are even or one is odd and other is even

def check(a,b):
    if a % 2 == 0 and b % 2 == 0:
        print("both are even")
    elif (a % 2 == 0 and b % 2 != 0) or (a % 2 != 0 and b % 2 == 0):
        print("one is odd and one is even")
    else:
        print("both are odd")

check(3,9)
        