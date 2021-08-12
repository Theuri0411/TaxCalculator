def cal_tax(gross_pay, tax):
    income_tax = gross_pay * tax / 100
    net_pay = gross_pay - income_tax
    return net_pay


def total_calc_tax(gross_pay, age):
    if 0 < age <= 45:
        return cal_tax(gross_pay, 9)
    elif 46 <= age <= 65:
        return cal_tax(gross_pay, 5)
    else:
        return cal_tax(gross_pay, 3)


print(total_calc_tax())
