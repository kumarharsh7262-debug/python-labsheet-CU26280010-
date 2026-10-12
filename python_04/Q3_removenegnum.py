# remove all negative numbers


numbers = [10, -5, 20, -2, 30]
result = []

for x in numbers:
    if x >= 0:
        result.append(x)

print("List =", result)