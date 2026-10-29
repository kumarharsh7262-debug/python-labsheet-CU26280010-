# delete student by rollnumber 

students = [
    {"roll": 1, "name": "Aman", "marks": 85},
    {"roll": 2, "name": "Ravi", "marks": 90}
]

roll = int(input("Enter roll number to delete: "))

for s in students:
    if s["roll"] == roll:
        students.remove(s)
        print("Student record deleted")
        break
else:
    print("Student not found")

print(students)