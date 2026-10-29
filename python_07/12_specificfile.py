# occurrence of a specific word in a file


f = open("data.txt", "r")
data = f.read()
word = input("Enter word: ")

count = data.split().count(word)
print("Occurrences =", count)

f.close()