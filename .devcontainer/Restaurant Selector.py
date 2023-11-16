#AP CSP
#Restaurant Selector
#Haani Khan
#Ask for Input
vegetarian = input("Are any of your party members vegetarian? ")
vegan = input("Are any of your party members vegan? ")
glutenfree = input("Are any of your party members gluten-free? ")

#LISTS
jgb = ["Joes Gourmet Burgers", "no", "no", "no"]
mspc = ["Main Street Pizza Company", "yes/no", "no", "yes/no"]
cc = ["Corner's Cafe", "yes/no", "yes/no", "yes/no"]
mfk = ["Mama's Fine Kitchen", "yes/no", "no", "no"]
tck = ["The Chef's Kitchen", "yes/no", "yes/no", "yes/no"]
restaurants = [jgb, mspc, cc, mfk, tck]

print("Your choices are... ")
for restaurant in restaurants:
    if vegetarian in restaurant[1] and vegan in restaurant[2] and glutenfree in restaurant[3]:
        print(restaurant[0])
    else:
        print("none :(")
        