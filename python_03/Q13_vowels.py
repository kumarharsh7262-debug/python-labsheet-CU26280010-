# Convert all vowels in a string to uppercase and consonants to lowercase

text = input("Enter a string: ")
result = ""

for char in text:
    if char.lower() in "aeiou":
        result += char.upper()
    else:
        result += char.lower()

print("Result =", result)