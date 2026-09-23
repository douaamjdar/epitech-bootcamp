while True:
    number, text = input("Enter an integer and a string: ").split()
    number = int(number)
    if number == 0:
        break
    lower = text.lower()
    if number >= 42 or "a" in lower or "e" in lower or "i" in lower or "o" in lower or "u" in lower:
        print(number)
    else:
        print(text)