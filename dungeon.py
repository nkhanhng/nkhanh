w = 4
h = 4

Matrix = [["-" for x in range(w)] for y in range(h)]

Matrix[1][1] = 'P'

for i in Matrix:
    print(*i,sep='  ')
mv = input("Your move: ").upper()


if mv == "A":
