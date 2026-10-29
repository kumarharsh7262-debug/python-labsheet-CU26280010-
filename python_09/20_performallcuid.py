# menu driven CRUD operation in list


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

while True:
    print("\n1. Add")
    print("2. View")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        r = int(input("Roll: "))
        n = input("Name: ")
        m = int(input("Marks: "))
        try:
            cur.execute("INSERT INTO students VALUES (?, ?, ?)", (r, n, m))
            con.commit()
            print("Record added")
        except sqlite3.IntegrityError:
            print("Roll number already exists")

    elif ch == 2:
        cur.execute("SELECT * FROM students")
        for row in cur.fetchall():
            print(row)

    elif ch == 3:
        r = int(input("Enter roll number: "))
        m = int(input("Enter new marks: "))
        cur.execute("UPDATE students SET marks=? WHERE roll=?", (m, r))
        con.commit()
        print("Record updated")

    elif ch == 4:
        r = int(input("Enter roll number: "))
        cur.execute("DELETE FROM students WHERE roll=?", (r,))
        con.commit()
        print("Record deleted")

    elif ch == 5:
        print("Program ended")
        break

    else:
        print("Invalid choice")

con.close()