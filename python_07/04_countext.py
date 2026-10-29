# Count the number of words in a text file

f = open("data.txt", "r")
data = f.read()

print("Words =", len(data.split()))
f.close()