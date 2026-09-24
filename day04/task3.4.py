message = input("Enter the message: ")
key_length = int(input("Enter the key length: "))
alphabet = "abcdefghijklmnopqrstuvwxyz"
common = "etaoinshr"
letters = ""
for character in message:
    if character in alphabet:
        letters += character
key = ""
for i in range(key_length):
    group = letters[i::key_length]
    best_shift = 0
    best_score = 0
    for shift in range(26):
        score = 0
        for letter in group:
            decrypted = alphabet[(alphabet.index(letter) - shift) % 26]
            if decrypted in common:
                score += 1
        if score > best_score:
            best_score = score
            best_shift = shift
    key += alphabet[best_shift]
result = ""
key_index = 0
for character in message:
    if character in alphabet:
        shift = alphabet.index(key[key_index % key_length])
        position = alphabet.index(character)
        result += alphabet[(position - shift) % 26]
        key_index += 1
    else:
        result += character
print("Key found:", key)
print(result)