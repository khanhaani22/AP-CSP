#Haani Khan
#Fraction Definer
print("# Proper Improper and Mixed Fractions")
print("#          By Haani Khan             ")
numerator = input("Input Numberator: ")
denominator = input("Input Denominator: ")

a = int(numerator) // int(denominator)
b = int(numerator) % int(denominator)
c = int(numerator)
d = int(denominator)

print("# Improper Fraction: " + str(c) + " / " + str(d))
print("# Mixed Number: " + str(a) + " + " + str(b) + " / " + str(d) ) 
