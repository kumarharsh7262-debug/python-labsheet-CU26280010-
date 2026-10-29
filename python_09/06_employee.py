# CRUD operation on employee

employees = {}

# Create
employees[1] = "Aman"
employees[2] = "Ravi"

# Read
print("Employees:", employees)

# Update
employees[1] = "Neha"
print("Updated:", employees)

# Delete
del employees[2]
print("After deletion:", employees)