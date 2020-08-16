exp = input()
lst = exp.split("+")
lst.sort()
result = ""
for x in range(len(lst)):
    result += (lst[x] + "+")
print(result[:-1])
