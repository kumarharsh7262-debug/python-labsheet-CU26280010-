
# common elements between two tuples

t1 = (10, 20, 30)
t2 = (20, 30, 40)

result = tuple(x for x in t1 if x in t2)
print(result)