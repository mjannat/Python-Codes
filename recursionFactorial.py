def recursion_factorial(n):
    if  n == 1 or n == 0:
        return 1
    else:
        return (n*recursion_factorial(n-1))
    
strg = input()
lst = strg.split(",")
result = ""
for x in range(len(lst)):
    val = recursion_factorial(int(lst[x]))
    result += str(val)
    result += ","
print(result[:-1])