def hour_format(hour, minute):
    if 24 > hour > 18 and 59 > minute > 00:
        print("Its P.M")
    else:
        print("Its A.M")

hour_format(1,  25)