# errors using exception handling

import sqlite3

try:
    con = sqlite3.connect("college.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM students")
    print(cur.fetchall())

    con.close()

except sqlite3.Error as e:
    print("Database error:", e)