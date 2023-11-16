#Financial Application: Payroll
#Haani Khan
print("#   Financial Application: Payroll   ")
print("#          By Haani Khan             ")

#Inputs
name = input("# Enter employee's name: ")
hours = input ("# Enter number of hours worked in a week: ")
payRate = input ("# Enter hourly pay rate: ")
fedRate = input ("# Enter federal tax witholding rate: ")
stateRate = input ("# Enter state tax withholding rate: ")
a = 0
otRate = 0
otHours = 0
extraPay = 0

#Overtime Math
if int(hours)>40:
    a = float(hours) // 40
    otRate = float(payRate) * 1.5
    otHours = float(hours) - (float(a)*40)
    extraPay = float(15.5) * float(otHours)

#Math
grossPay = str(((float(hours) - otHours) * float(payRate)) + extraPay)
fedWith = str(float(grossPay) * float(fedRate))
stateWith = str(float(grossPay) * float(stateRate))
totalDeducts = str(float(fedWith) + float(stateWith))
netPay = str(float(grossPay) - float(totalDeducts))

#Outputs
print("Employee Name: " + name)
print("Hours Worked: " + hours)
print("Pay Rate: $" + payRate)
print("Gross Pay: $" + grossPay)
print("Overtime Hours: " + str(otHours))
print("Overtime Pay: $" + str(extraPay))
print("Deductions: ")
print("   Federal Witholding (" + str(100 * float(fedRate)) +"%): $" + fedWith)
print("   State Witholding (" + str(100 * float(stateRate)) + "%): $" + stateWith)
print("   Total Deductions: " + totalDeducts)
print("Net Pay: " + netPay)