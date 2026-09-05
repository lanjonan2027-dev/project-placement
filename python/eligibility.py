def check_tax_eligibility(age, income):
    if age > 18 and income > 500000:
        print("Eligible for tax")
    else:
        print("Not eligible for tax")


age = int(input("Enter your age: "))
income = float(input("Enter your income: "))

check_tax_eligibility(age, income)