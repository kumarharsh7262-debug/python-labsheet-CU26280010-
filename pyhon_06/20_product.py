

s1 = {1, 2}
s2 = {'A', 'B'}

result = {(x, y) for x in s1 for y in s2}
print("Cartesian product =", result)