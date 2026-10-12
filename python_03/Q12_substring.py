# Check if a substring exists in a given string

text = input("Enter a string: ")
substring = input("Enter substring: ")

if substring in text:
    print("Substring exists")
else:
    print("Substring does not exist")