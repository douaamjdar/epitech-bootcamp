text = input("Enter a sentence: ").lower()
words = ["cat", "garden", "mice"]
total = 0
for word in words:
    total = total + text.count(word)
    reversed_word = word[::-1]
    total = total + text.count(reversed_word)
print(total)