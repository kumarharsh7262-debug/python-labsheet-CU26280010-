# update a studet marks 

students = [
    {"roll": 1, "name": "Aman", "marks": 85},
    {"roll": 2, "name": "Ravi", "marks": 90}
]

roll = int(input("Enter roll number: "))
marks = int(input("Enter new marks: "))

for s in students:
    if s["roll"] == roll:
        s["marks"] = marks
        print("Marks updated:", s)
        break
else:
    print("Student not found")