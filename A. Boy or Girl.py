from collections import defaultdict

text_dict = defaultdict(int)

text = input()
cnt = 0
for x in range(len(text)):
    temp = text_dict.get(text[x])
    if temp != 1:
        cnt += 1
        text_dict[text[x]] = 1

if cnt % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
