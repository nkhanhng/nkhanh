

def count(list):
    c = 0

    for i in list:
        if len(i) >= 2 and i[0] == i[-1]:
                c += 1
    return c

print(count(['abc','xyz','aba','1221']))
