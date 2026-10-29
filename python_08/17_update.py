# Update the name of a student

import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute(
    "UPDATE students SET name=? WHERE id=?",
    ("Arjun", 1)
)

con.commit()
print("Name updated")

con.close()