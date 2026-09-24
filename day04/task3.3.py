message = input("Enter a message: ")
key = input("Enter a key: ").lower().strip()
mode = input("Encrypt or decrypt? (e/d): ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
result = ""
key_index = 0
for letter in message:
    if letter in alphabet:
        shift = alphabet.index(key[key_index % len(key)])
        if mode == "d":
            shift = -shift
        position = alphabet.index(letter)
        result += alphabet[(position + shift) % 26]
        key_index += 1
    else:
        result += letter
print(result)