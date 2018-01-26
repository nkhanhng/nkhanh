def sum_even(n):
    count = 0
    for i in range(-n - 1, 0):
        count = count + i
    return count

s = sum_even(4)
print(s)
