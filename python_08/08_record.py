# Insert a single record into the students table

import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute(
    "INSERT INTO students VALUES (?, ?, ?, ?)",
    (1, "Aman", 21, 85)
)

con.commit()
print("Record inserted")

con.close()