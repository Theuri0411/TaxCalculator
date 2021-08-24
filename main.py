# #TaxCalculator
#
# gross_salary = 40000
# loan = 3000
# sacco = 2000
#
# age = (input("enter age: "))
# if age <=18:
#     result = gross_salary * 3/100
# elif age > 18 and age <= 24:
#     result = gross_salary * 6/100
# elif age > 24 and age <= 35:
#     result = gross_salary * 8/100
# elif age > 35 and age <= 40:
#     result = gross_salary * 16/100
# elif age > 40 and age <= 55:
#     result = gross_salary * 12/100
# elif age > 55:
#     result = gross_salary * 3/100
# else:
#     print("Did not enter age")
#
#
# taxed_return = gross_salary-result
# sum_total = taxed_return-loan-sacco
# print(sum_total)
#

#
# #GRADING SYSTEM#
#
#
# while True:
#     marks_input = int(input("input marks: "))
#     print("User entered", marks_input)
#     isinteger = isinstance(marks_input, int)
#     print(isinteger)

#     if marks_input >= 91 and marks_input <=100:
#         print("A")
#     elif marks_input >= 81 and marks_input <= 90:
#         print("B")
#     elif marks_input >= 71 and marks_input<= 80:
#         print("C")
#     elif marks_input >= 61 and marks_input<= 70:
#         print("D")
#     elif marks_input >= 51 and marks_input <= 60:
#         print("E")
#     elif marks_input >= 41 and marks_input <= 50:
#         print("F")
#     else:
#         print("FAIL")
#
import time
import os
import sys
import math
##from colorama import Fore, Back, Style
from datetime import datetime
from datetime import timedelta

challengetime = int(input("ENTER EXPECTED CODING TIME IN HOURS : "))
if challengetime < 0 or challengetime == 0:
    print("BE REALISTIC MAN ...")
else:
    counter = 0
    timeoffinish = datetime.now() + timedelta(hours=challengetime)
    countertime = time.ctime()
    while True:
        seconds = counter % 60
        minutes = counter / 60 % 60
        hours = counter / 3600 % 60
        if (math.ceil(challengetime - math.ceil(hours) - 1) < 1 and (59 - math.ceil(minutes) < 1) and (
                59 - math.ceil(seconds)) < 1):
            print("\n")
            print("Time Is Up Dev,Take A rest.You Have 3 Seconds TO SAVE YOUR WORK  SOLDIER")
            time.sleep(5)
            os.system('killall code')
            print("Sleeping In 5 Seconds ...")
            time.sleep(5)
            os.system('poweroff')
        else:
            print("START TIME   : " + countertime + "\n")
            print("FINISH LINE  : " + str(timeoffinish.strftime("%c")) + "\n")
            print("CURRENT TIME : " + time.ctime() + "\n")
            print("TIME REMAINING : " + str(math.ceil(challengetime - math.ceil(hours) - 1)) + " Hours "
                  + str(59 - math.ceil(minutes)) + " Minutes " + str(59 - math.ceil(seconds)) + "  Seconds" + "\n")
            print("You Have Been CODING For => " + str(math.ceil(hours)) + " HOURS : " + str(
                math.ceil(minutes)) + " MINUTES : "
                  + str(math.ceil(seconds + 1) % 60) + " SECONDS ")
            counter = counter + 1
            time.sleep(1)
            os.system('clear')

