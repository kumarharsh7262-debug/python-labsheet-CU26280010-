# insert a new record

import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute(
    "INSERT OR REPLACE INTO students VALUES (?, ?, ?)",
    (1, "Aman", 85)
)

con.commit()
print("Record inserted")
con.close()