#Haani Khan
#Nested and While Loops
num = 1
main1 = 0
switch = 0
while (switch == 0):
    num = int(input("Input number greater than 0: "))
    
    for i in range(num):
        print("*" * (num - i))
    
    switch = int(input("Would you like to rerun the program? (0 to continue, 1 to quit)"))