# most repeated word

text = input("Enter a string: ")
words = text.split()

most = max(words, key=words.count)

print("Most repeated word =", most)