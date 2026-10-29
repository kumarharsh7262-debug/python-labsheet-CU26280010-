# search for a student record

import csv

name = input("Enter student name: ")
found = False

with open("student.csv", "r") as f:
    r = csv.DictReader(f)

    for row in r:
        if row["Name"].lower() == name.lower():
            print(row)
            found = True

if not found:
    print("Record not found")