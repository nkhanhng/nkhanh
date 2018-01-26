def count_odd(n):
    count = 0
    for i in range(n+1):
        if i % 2 == 0:
            continue
        else:
            count = count + 1
    return count

c = count_odd(10)
print(c)
