# repeated items in a tuple

t = (10, 20, 10, 30, 20, 40)
result = tuple(x for x in dict.fromkeys(t) if t.count(x) > 1)
print(result)