sentence = input("Enter a sentence: ")
words = sentence.split()
letters = [word[0] for word in words]
result = ''.join(letters)
print(result)