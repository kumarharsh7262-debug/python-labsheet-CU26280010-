# Import CSV data into a database table


import sqlite3
import csv

con = sqlite3.connect("college.db")
cur = con.cursor()

with open("students.csv", "r") as f:
    r = csv.reader(f)
    next(r)

    cur.executemany(
        "INSERT INTO students VALUES (?, ?, ?, ?)",
        [(int(a), b, int(c), float(d)) for a, b, c, d in r]
    )

con.commit()
con.close()

print("CSV data imported")
