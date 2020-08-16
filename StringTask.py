text = input()
text = text.lower()
strg = ""
vowel = ['a', 'e', 'i', 'o', 'u', 'y']
for i in range(0, len(text)):
    if text[i] not in vowel:
        strg += '.'
        strg += text[i]

print(strg)