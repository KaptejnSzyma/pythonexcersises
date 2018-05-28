text = input("Type something: ")
text_set = set(text)
vowels = {"a", "e", "i", "o", "u", "y", "i", " "}
print(sorted(text_set.difference(vowels)))
