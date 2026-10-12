# Find the key with maximum value

data = {"a": 10, "b": 50, "c": 30}
key = max(data, key=data.get)

print("Maximum value key =", key)