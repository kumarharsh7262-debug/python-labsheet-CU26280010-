# reverse string 

text = input("Enter string:")
reverse = ""

for char in text:
    reverse = char + reverse
print(reverse)


