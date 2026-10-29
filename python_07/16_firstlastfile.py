#  first and last lines of a file


f = open("data.txt", "r")
lines = f.readlines()
f.close()

if lines:
    print("First line:", lines[0].strip())
    print("Last line:", lines[-1].strip())
else:
    print("File is empty")
