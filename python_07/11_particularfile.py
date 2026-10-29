# particular word in a file 

f = open("data.txt", "r")
data = f.read()
word = input("Enter word to search: ")

if word in data:
    print("Word found")
else:
    print("Word not found")

f.close()