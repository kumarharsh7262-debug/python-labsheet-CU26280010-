# Connect to Database and Create Students Table

import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    roll INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

con.commit()
print("Table created successfully")
con.close()