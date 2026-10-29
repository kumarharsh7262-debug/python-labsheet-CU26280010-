# INNER JOIN between students and courses


import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("""
SELECT students.name, courses.course
FROM students
INNER JOIN courses
ON students.id = courses.student_id
""")

for row in cur.fetchall():
    print(row)

con.close()