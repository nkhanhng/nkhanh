a = [10,20,30,20,10,50,60,40,80,50,40]

dup = []
uni = []

for i in a:
    if i not in dup:
        dup.append(i)
        uni.append(i)

print(uni)
