# Display Records Sorted by Student Name

import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("SELECT * FROM students ORDER BY name ASC")

for row in cur.fetchall():
    print(row)

con.close()