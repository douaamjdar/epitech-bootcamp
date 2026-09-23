sentence = "tutu on the tuki-kata"
result = ""

for char in sentence:
    result += char
    if result.endswith("tu"):
        result = result[:-2] + "ta"

print(result)