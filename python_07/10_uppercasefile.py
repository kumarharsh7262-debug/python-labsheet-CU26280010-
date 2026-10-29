# convert its content to uppercase


f = open("data.txt", "r")
data = f.read()
f.close()

print(data.upper())