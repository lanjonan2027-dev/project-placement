def clock_angle(hours, minutes):
    minute_angle = minutes * 6
    hour_angle = (hours % 12) * 30 + minutes * 0.5

    difference = abs(hour_angle - minute_angle)

    if difference > 180:
        difference = 360 - difference

    return difference


hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))

angle = clock_angle(hours, minutes)

print("Smaller angle:", angle, "degrees")