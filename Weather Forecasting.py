#Haani Khan
#Define functions
def probability(pA):
    if 0.8 <= pA <= 1:
        return "high"
    elif 0.6 <= pA <= 0.79:
        return "medium"
    elif 0.4 <= pA <= 0.59:
        return "low"

#Input Rainfall Values
dryDays = 0
rain = 0
totalRain = 0
for i in range(5):
    rain = float(input("How much rainfall occurned on day " + str(i+1) + ": "))
    totalRain += rain
    if rain == 0:
        dryDays += 1
pA = (5 - dryDays) / 5

#Output
print("Tomorrow there is a " + probability(pA) + " probability with a " + format(pA, "0.0%") + " chance of rain.")
if totalRain > 15:
    print("The reservoir's capacity is full.")
else:
    print("Drough conditions are still in place.")