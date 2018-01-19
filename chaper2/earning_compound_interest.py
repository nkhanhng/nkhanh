#A = P * (1+r/n)^nt

P = 10000
n = 12
r = 0.08
t = int(input("How many years?"))

A = P * (1 + r/n) **(n*t)
print("The final amount after", t," year(s) is", A)
