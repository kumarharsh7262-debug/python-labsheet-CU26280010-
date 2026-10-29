# delete student using rll no 


import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

roll = int(input("Enter roll number to delete: "))
cur.execute("DELETE FROM students WHERE roll=?", (roll,))

con.commit()
print("Record deleted")
con.close()