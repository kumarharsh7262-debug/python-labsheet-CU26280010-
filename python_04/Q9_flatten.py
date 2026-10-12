# Flatten a nested list

nested = [[1, 2], [3, 4], [5, 6]]
flat = []

for sublist in nested:
    for x in sublist:
        flat.append(x)

print("Flattened list =", flat)