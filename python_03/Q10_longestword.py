# longest word in a string

text = input("Enter a string: ")
words = text.split()

longest = max(words, key=len)

print("Longest word =", longest)