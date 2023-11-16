#Haani Khan
rate = 0.06
n = 365.00

principal = float(input("What is the principal amount? "))
years = float(input("How many years?"))
A = principal * pow((1 + ( rate / n )), ( n * years))

print("You have to pay " + str(A) + " with " + str(A - principal) + " as interest.")