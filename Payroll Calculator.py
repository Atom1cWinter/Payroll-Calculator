#Payroll Calculator
##A copy of Rickey's GitHub repository rewritten in Python

print ('This is a payroll calculator! It will factor in overtime pay at the standard time and a half.\n')

hours_worked = float(input("Please enter the amount of hours worked this week:\n"))
pay_rate = float(input("Please enter the payrate for this employee:\n"))

total_pay = 0

if hours_worked > 40:
    total_pay = ((hours_worked - 40.00) * (1.5 * pay_rate)) + (40 * pay_rate)
else:
    total_pay  = hours_worked * pay_rate

rounded_total_pay = round(total_pay, 2) #Cannot for the life of me get this to save to the second decimal place so we're leaving it as is.

print ("Employee's pay (before tax) is ${}.".format(rounded_total_pay))