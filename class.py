import math
import csv

with open('data.csv',newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]
def mean(data):
    n = len(data)
    total = 0

    for x in data:
        total += int(x)

    mean = total / n
    return mean

squared = []

for number in data:
    a = int(number) - mean(data)
    a = a**2
    squared.append(a)

sum = 0

for i in squared:
    sum = sum + i
result = sum / (len(data)-1)
std_dev = math.sqrt(result)
print (std_dev)