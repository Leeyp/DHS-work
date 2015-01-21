__author__ = 'dhs'
name = input("Enter name: ")
hours = input("Enter number of hours worked weekly: ")
payrate = input("Enter hourly pay rate: ")
CPF = input("Enter CPF contribution rate (%): ")

print("Payroll statement for", name)
print("Number of hours worked in week:", hours)
print("Hourly pay rate: $" + payrate)
print("Gross Pay: ${:.2f}".format(float(hours)*float(payrate)))
print("CPF contribution at", CPF+"% = ${:.2f}".format(round(float(hours)*float(payrate)*float(CPF)/100,3)))
print(" ")
print("Net pay: ${:.2f}".format(round(float(hours)*float(payrate)*(100-float(CPF))/100,3)))