# structure of the students table

import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("PRAGMA table_info(students)")

for row in cur.fetchall():
    print(row)

con.close()