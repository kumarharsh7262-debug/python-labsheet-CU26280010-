#frequency

text = input("Enter a string: ")
for char in set(text):
    print(char, ":", text.count(char))

