
import csv

with open("student.csv", "r") as f:
    r = csv.DictReader(f)

    for row in r:
        print(row["Name"], row["Marks"])