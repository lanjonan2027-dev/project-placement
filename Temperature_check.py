#Temperature check Cold, warm or Hot

def temperature_check(temp):
    if temp < 10:
        print("Cold")
    elif temp >= 10 and temp <= 30:
        print("Warm")
    else:
        print("Hot")

temperature_check(40) 