import sqlite3
import csv

con = sqlite3.connect("college.db")
cur = con.cursor()
cur.execute("SELECT * FROM students")

with open("students.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "name", "age", "marks"])
    w.writerows(cur.fetchall())

con.close()
print("Data exported to CSV")