# create a new database 

import sqlite3

con = sqlite3.connect("student.db")
print("Database created successfully")

con.close()