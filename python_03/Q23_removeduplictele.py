#  Remove duplicate elements

numbers = [1, 2, 2, 3, 4, 4, 5]
result = []

for x in numbers:
    if x not in result:
        result.append(x)

print("List after removing duplicates =", result)