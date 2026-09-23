message = input("Enter a message: ")
key = int(input("Enter a key: "))
alphabet = "abcdefghijklmnopqrstuvwxyz"
result = ""
for letter in message:
    if letter in alphabet:
        position = alphabet.index(letter)
        new_position = (position + key) % 26
        result += alphabet[new_position]
    else:
        result += letter
print(result)