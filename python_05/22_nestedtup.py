# Flatten a nested tuple

t = ((1, 2), (3, 4), (5, 6))
result = tuple(x for sub in t for x in sub)
print(result)