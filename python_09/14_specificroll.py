# search student by roll no 

import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

roll = int(input("Enter roll number: "))
cur.execute("SELECT * FROM students WHERE roll=?", (roll,))

print(cur.fetchone())
con.close()