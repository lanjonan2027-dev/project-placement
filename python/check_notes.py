def check_notes(amount):
    if amount % 100 == 0:
        print("Can be equally divided into 2000, 500 and 100 notes")
    else:
        print("Cannot be divided equally")

check_notes(100)