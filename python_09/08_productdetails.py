# Store and Manage Product Details Using CRUD Operations

products = {}

# Create
products[1] = "Laptop"
products[2] = "Mobile"

# Read
print("Products:", products)

# Update
products[1] = "Computer"
print("Updated:", products)

# Delete
del products[2]
print("After deletion:", products)