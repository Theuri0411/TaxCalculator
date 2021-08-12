
import tax_calculator as tc


while True:
    try:
        name = str(input("Enter your name: \n"))
        try:
            age = int(input("Enter your name: \n"))
            gross_pay = int(input("Enter your pay: \n)")
            net_pay = tc.total_calc_tax((gross_pay, age))
            print(name, "Your take away home salary is ,", "ksh:", net_pay)
        except ValueError:
            print("Invalid data")
    except KeyboardInterrupt:
        print("This program was stopped by the user")
        exit()
