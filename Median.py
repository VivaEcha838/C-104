import csv

with open('height-weight.csv', newline= '') as f:
    readfile = csv.reader(f)
    file_data = list(readfile)

file_data.pop(0)

new_data = []
for i in range(len(file_data)):
    height = file_data [i][1]
    new_data.append(float(height))

n = len(new_data)

new_data.sort()

if n%2 == 0:
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2-1])

    median = (median1 + median2)/2

else:
    median = new_data[n//2]

print("Median is : " + str(median)) 