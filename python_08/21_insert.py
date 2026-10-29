import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS courses (
    student_id INTEGER,
    course TEXT
)
""")

cur.executemany("INSERT INTO courses VALUES (?, ?)", [
    (1, "Python"),
    (2, "Java"),
    (3, "DBMS")
])

con.commit()
print("Courses created and data inserted")

con.close()