message = input("Enter message: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
for key in range(1, 26):
    result = ""
    for letter in message:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - key) % 26
            result += alphabet[new_position]
        else:
            result += letter
    print(key, result)