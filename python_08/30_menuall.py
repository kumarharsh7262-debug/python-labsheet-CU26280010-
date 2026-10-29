# Menu-driven student management application


import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    marks REAL
)
""")

while True:
    print("\n1. Add  2. View")
    print("3. Update  4. Delete  5. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        i = int(input("Enter ID: "))
        n = input("Enter name: ")
        a = int(input("Enter age: "))
        m = float(input("Enter marks: "))

        cur.execute(
            "INSERT INTO students VALUES (?, ?, ?, ?)",
            (i, n, a, m)
        )
        con.commit()
        print("Student added")

    elif ch == "2":
        cur.execute("SELECT * FROM students")
        for row in cur.fetchall():
            print(row)

    elif ch == "3":
        i = int(input("Enter ID: "))
        m = float(input("Enter new marks: "))

        cur.execute(
            "UPDATE students SET marks=? WHERE id=?",
            (m, i)
        )
        con.commit()
        print("Student updated")

    elif ch == "4":
        i = int(input("Enter ID: "))
        cur.execute("DELETE FROM students WHERE id=?", (i,))
        con.commit()
        print("Student deleted")

    elif ch == "5":
        break

    else:
        print("Invalid choice")

con.close()