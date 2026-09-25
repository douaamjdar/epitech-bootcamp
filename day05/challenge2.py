scores = {"AEIOULNSTR": 1, "DG": 2, "BCMP": 3, "FHVWY": 4, "K": 5, "JX": 8, "QZ": 10}
def scrabble_score(word):
    total = 0
    for letter in word.upper():
        for letters in scores:
            if letter in letters:
                total = total + scores[letters]
    return total
print(scrabble_score("epitech"))