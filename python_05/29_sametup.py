# check element in a tuple are same

t = (5, 5, 5, 5)

if len(set(t)) == 1:
    print("All elements are same")
else:
    print("Elements are different")