# Remove duplicate values

data = {"a": 1, "b": 2, "c": 1}
result = {}

for k, v in data.items():
    if v not in result.values():
        result[k] = v

print(result)