#  longest line in a file


f = open("data.txt", "r")
lines = f.readlines()
f.close()

if lines:
    print("Longest line =", max(lines, key=len).strip())