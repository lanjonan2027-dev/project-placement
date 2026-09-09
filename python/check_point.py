def check_point(x, y):
    if x == 0 and y == 0:
        print("The point lies at the origin.")
    elif y == 0:
        print("The point lies on the X-axis.")
    elif x == 0:
        print("The point lies on the Y-axis.")
    else:
        print("The point lies neither on the X-axis nor Y-axis.")


x = int(input("Enter x-coordinate: "))
y = int(input("Enter y-coordinate: "))

check_point(x, y)