#Classifying grades according to the marks

def classify_grade(marks):
    if marks >= 90 and marks <= 100:
        print("The grade is A.")

    elif marks >= 80 and marks < 90:
        print("The grade is B.")

    elif marks >= 70 and marks < 80:
        print("The grade is C.")

    elif marks >= 60 and marks < 70:
        print("The grade is D.")

    elif marks < 60:
        print("The grade is F.")

    else:
        print("Invalid marks. Please enter a value between 0 and 100.")

classify_grade(110)