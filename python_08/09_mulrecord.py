# Insert multiple records into the students table

import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

data = [
    (2, "Ravi", 22, 90),
    (3, "Neha", 21, 75),
    (4, "Priya", 20, 35)
]

cur.executemany(
    "INSERT INTO students VALUES (?, ?, ?, ?)", data
)

con.commit()
print("Records inserted")

con.close()