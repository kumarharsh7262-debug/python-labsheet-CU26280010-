# even-numbered lines from a file

f = open("data.txt", "r")

for i, line in enumerate(f, 1):
    if i % 2 == 0:
        print(line, end="")

f.close()