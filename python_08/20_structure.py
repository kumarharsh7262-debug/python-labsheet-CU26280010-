import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("DELETE FROM students")

con.commit()
print("Table emptied")

con.close()