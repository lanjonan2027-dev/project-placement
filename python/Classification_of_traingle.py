#Classifying traingle based on the sides

def classify_triangle(a, b, c):

    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("The given sides can form an equilateral triangle.")

        elif a == b or b == c or a == c:
            print("The given sides can form an isosceles triangle.")

        else: 
            print("The given sides can form a scalene triangle.")

    elif a == 0 or b == 0 or c == 0:
        print("The sides cannot be zero.")

    else:
        print("The given sides cannot form a valid triangle.")

classify_triangle(3, 3, 4)
