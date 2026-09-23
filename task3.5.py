text = input("Enter text: ").lower()
total = 0
for char in text:
    if char.isalpha():
        total += 1
found_letters = ""
for char in text:
    if char.isalpha() and char not in found_letters:
        found_letters = found_letters + char
percentages = {}
for letter in found_letters:
    count = text.count(letter)
    percentage = count / total * 100
    percentages[letter] = percentage
    print(letter, ":", round(percentage, 1), "%")
english = {"e":12.7,"t":9.1,"a":8.2,"o":7.5,"i":7.0,"n":6.7,"s":6.3,"h":6.1,"r":6.0,"d":4.3,"l":4.0,"c":2.8,"u":2.8,"m":2.4,"w":2.4,"f":2.2,"g":2.0,"y":2.0,"p":1.9,"b":1.5,"v":1.0,"k":0.8,"j":0.15,"x":0.15,"q":0.1,"z":0.07}
german = {"e":16.4,"n":9.8,"i":7.6,"s":7.3,"r":7.0,"a":6.5,"t":6.2,"d":5.1,"h":4.8,"u":4.4,"l":3.4,"c":3.1,"g":3.0,"m":2.5,"o":2.5,"b":1.9,"w":1.9,"f":1.7,"k":1.2,"z":1.1,"p":0.8,"v":0.7,"j":0.3,"y":0.04,"x":0.03,"q":0.02,"ü":0.7,"ö":0.3,"ä":0.5,"ß":0.3}
turkish = {"a":12.9,"e":8.9,"i":8.6,"n":7.5,"r":6.7,"l":5.9,"k":4.7,"d":4.9,"t":3.3,"s":3.0,"m":3.7,"y":3.3,"u":3.2,"o":2.5,"b":2.8,"ü":1.9,"ş":1.8,"g":1.3,"z":1.5,"h":1.2,"c":1.1,"ç":1.2,"p":0.9,"ö":0.8,"v":1.0,"ğ":1.1,"ı":5.1,"f":0.5,"j":0.03}
languages = {"English": english, "German": german, "Turkish": turkish}
best_language = ""
best_score = -1
for lang_name in languages:
    lang_freq = languages[lang_name]
    score = 0
    for letter in lang_freq:
        text_pct = percentages.get(letter, 0)
        diff = abs(text_pct - lang_freq[letter])
        score = score + diff
    if best_score == -1 or score < best_score:
        best_score = score
        best_language = lang_name
print("Detected language:", best_language)