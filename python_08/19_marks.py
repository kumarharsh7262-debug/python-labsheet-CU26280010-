# Delete all students with marks below 40

import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("DELETE FROM students WHERE marks < 40")

con.commit()
print("Low-mark records deleted")

con.close()
