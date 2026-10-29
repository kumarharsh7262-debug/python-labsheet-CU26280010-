# new record to an existing CSV file

import csv

with open("student.csv", "a", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Neha", 85])

print("Record added")