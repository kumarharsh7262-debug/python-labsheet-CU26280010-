# creat and write into CSV

import csv

with open("student.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Name", "Marks"])
    w.writerow(["Aman", 80])
    w.writerow(["Ravi", 90])

print("CSV file created")