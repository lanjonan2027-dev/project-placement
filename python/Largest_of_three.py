# Printing largest out of three numbers

def Largest(a, b, c):
    if (a>b) and (a>c):
        print("Largest:", a)
    elif (b>a) and (b>c):
        print("Largest:", b)
    else:
        print("Largest:", c)

Largest(10, 20, 30)