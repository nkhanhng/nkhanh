def sum_to(n):
    total = 0
    for i in range(n+1):
        total = total + i
    return total

m = int(input("number"))
s = sum_to(m)
print(s)
