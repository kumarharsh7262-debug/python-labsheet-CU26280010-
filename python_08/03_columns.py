# create a table name student 

import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER,
    name TEXT,
    age INTEGER,
    marks REAL
)
""")

con.commit()
print("Table created successfully")

con.close()