#  Calculate the average of numeric columns in a CSV file


import csv

total = 0
count = 0

with open("student.csv", "r") as f:
    r = csv.reader(f)
    next(r)

    for row in r:
        total += float(row[1])
        count += 1

if count:
    print("Average =", total / count)
