#Extract uppercases characters
text = input("Enter a string: ")
for ch in  text: 
    if ch.isupper():
        print(ch, end=" ")