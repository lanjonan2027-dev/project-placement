#Check if one of two given numbers is a multiple of the other. 

def multiple(a,b):
    if a % b == 0 or b % a == 0:
        print("One number is a multiple of other")
    else:
        print("No multiples found")

multiple(10,3)
