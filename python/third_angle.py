def third_angle(angle1, angle2):
    angle3 = 180 - angle1 -angle2
    return angle3

angle1 = float(input("enter first angle"))
angle2 = float(input("enter second angle"))
angle3 = third_angle(angle1, angle2)

print(angle3)