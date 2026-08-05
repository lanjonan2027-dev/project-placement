#Taking three sides and checking if they can form a valid triangle or not

def is_valid_triangle(a, b, c):

    if a + b > c and a + c > b and b + c > a:
        print("The given sides can form a valid triangle.")

    elif a == 0 or b == 0 or c == 0:
        print("The sides cannot be zero.")

    else:
        print("The given sides cannot form a valid triangle.")

is_valid_triangle(1,1,3)