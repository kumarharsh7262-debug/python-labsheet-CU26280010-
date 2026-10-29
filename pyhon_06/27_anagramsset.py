# two strings are anagrams using sets

s1 = "listen"
s2 = "silent"

if len(s1) == len(s2) and set(s1) == set(s2):
    print("Anagrams")
else:
    print("Not anagrams")