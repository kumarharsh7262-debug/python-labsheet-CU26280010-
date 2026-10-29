# duplicate elements in a list using a set

lst = [10, 20, 10, 30, 20, 40]

seen = set()
duplicates = set()

for x in lst:
    if x in seen:
        duplicates.add(x)
    else:
        seen.add(x)

print("Duplicates =", duplicates)