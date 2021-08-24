#Practice Calc

gross_salary = 40000
loan = 3000
sacco = 2000

age = int(input("enter age: "))
if age <= 18:
    result = gross_salary * 3 / 100
elif 18 < age <= 24:
    result = gross_salary * 6 / 100
elif 24 < age <= 35:
    result = gross_salary * 8 / 100
elif 35 < age <= 40:
    result = gross_salary * 16 / 100
elif 40 < age <= 55:
    result = gross_salary * 12 / 100
else:
    result = 0

taxed_return = gross_salary - result
sum_total = taxed_return - loan - sacco
print(sum_total)


def totalpay(age=int(input("enter age: ")), gross_salary=int(input("enter salary: "))):
    sacco = 500
    loan = 1000
    deductions = loan + sacco
    if 0 < age <= 45:
        tax = gross_salary * (9 / 100)
        net_pay = gross_salary - tax - deductions
        print(net_pay)


print(totalpay())
