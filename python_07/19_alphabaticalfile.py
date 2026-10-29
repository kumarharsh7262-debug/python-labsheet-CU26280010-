# all words alphabetically and save to a new file

f = open("data.txt", "r")
words = f.read().split()
f.close()

words.sort()

f = open("sorted.txt", "w")
f.write(" ".join(words))
f.close()

print("Words sorted successfully")
