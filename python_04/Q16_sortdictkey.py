# sort dict by key 

data = {"a": 3, "b": 1, "c": 2}
sorted_data = dict(sorted(data.items(), key=lambda x: x[1]))

print(sorted_data)