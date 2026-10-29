# rows and columns in a CSV file

import csv

with open("student.csv", "r") as f:
    rows = list(csv.reader(f))

print("Rows =", len(rows))
print("Columns =", len(rows[0]) if rows else 0)