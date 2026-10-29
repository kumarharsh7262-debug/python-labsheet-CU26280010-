#sum of two tuple 

t1 = (10, 20, 30)
t2 = (1, 2, 3)

result = tuple(a + b for a, b in zip(t1, t2))
print(result)