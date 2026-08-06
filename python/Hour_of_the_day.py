#Taking Hour of the day and printing the greeting message according to the hour of the day

def greeting(hour):
    if hour < 12:
        return print("Good Morning!")
    elif hour < 18:
        return print("Good Afternoon!")
    elif hour < 24:
        return print("Good Evening!")
    else:
        return "Invalid hour! Please enter a valid hour between 0 and 23."

greeting(22)
    