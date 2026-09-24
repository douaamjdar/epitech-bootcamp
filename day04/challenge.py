while True:
    number, text = input("Enter an integer and a string: ").split()
    number = int(number)
    if number == 0:
        break
    vowel = text.lower()
    if number >= 42 or "a" in vowel or "e" in vowel or "i" in vowel or "o" in vowel or "u" in vowel:
        print(number)
    else:
        print(text)