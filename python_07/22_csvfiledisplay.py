#  reade data from CSV file

import csv

with open("student.csv", "r") as f:
    r = csv.reader(f)
    for row in r:
        print(row)