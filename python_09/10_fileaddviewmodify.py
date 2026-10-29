# CRUD Operations on a File

file = "records.txt"

# Add
with open(file, "w") as f:
    f.write("1 Aman 85\n")
    f.write("2 Ravi 90\n")

# View
with open(file, "r") as f:
    print("Records:", f.read())

# Modify
with open(file, "r") as f:
    data = f.read()

data = data.replace("Aman 85", "Aman 95")

with open(file, "w") as f:
    f.write(data)

# Delete record
with open(file, "r") as f:
    lines = f.readlines()

with open(file, "w") as f:
    for line in lines:
        if not line.startswith("2 "):
            f.write(line)

print("Final records:")
with open(file, "r") as f:
    print(f.read())