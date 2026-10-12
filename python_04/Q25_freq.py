# Count word frequency in a paragraph

text = "python is easy python is useful"
words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)