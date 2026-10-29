# Delete a student record using ID

import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("DELETE FROM students WHERE id=?", (4,))

con.commit()
print("Record deleted")

con.close()