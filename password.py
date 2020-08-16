import re
strg = input()
lst = strg.split(",")
print(lst)
result = ""
flag = 0
x = 0
while x < len(lst):
    password = str(lst[x])
    while True:
        if len(password) < 6 or len(password) > 12:
            flag = -1
            break
        elif not re.search("[a-z]", password):
            flag = -1
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            break
        elif not re.search("[0-9]", password):
            flag = -1
            break
        elif not re.search("[#@$]", password):
            flag = -1
            break
        else:
            flag = 0
            break
    if flag == 0:
        result += password
        result += ","
    x += 1

print(result[:-1])