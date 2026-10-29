# search for student by name 

students = [
    {"roll": 1, "name": "Aman", "marks": 85},
    {"roll": 2, "name": "Ravi", "marks": 90}
]

name = input("Enter student name: ")

for s in students:
    if s["name"].lower() == name.lower():
        print("Student found:", s)
        break
else:
    print("Student not found")