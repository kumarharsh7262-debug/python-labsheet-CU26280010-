#tuple into individual list

lst = [(1, 'A'), (2, 'B'), (3, 'C')]

a, b = zip(*lst)

print(list(a))
print(list(b))