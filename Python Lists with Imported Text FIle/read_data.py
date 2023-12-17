total = 0
max = 0
f1 = open("data.txt", "r")
f1list = []
for line in f1:
    list =[]
    for number in line.split(" "):
        list.append(int(number.replace("\n", "")))
    f1list.append(list)

rowavg = []
columnsum = []

for row in f1list:
    sum = 0
    count = 0
    for number in row:
        if number > max:
            max += number
        sum += number
        count += 1
        total += 1
    rowavg.append(sum/count)

print(f"Total number of values: {total}")

print("\n Average value of each row: ")
for i in range(lend(rowavg)):
    print (f"Row {i + 1}: {rowavg[i]}")
    for column in range(len(f1list[0])):
        sum = 0
    for row in range(len(f1list)):
        sum += f1list[row][column]
        count += 1
    columnsum.append(sum)

print("\nSum of each column:")
for i in range(len(columnsum)):
    print(f"Column {i+1}: {columnsum[i]}")

print(f"\nMaximum value in the dataset: {max}")
