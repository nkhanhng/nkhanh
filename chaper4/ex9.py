from turtle import *

def star(n,s):
    for i in range(n):
        forward(s)
        right(144)

        
for i in range(5):
    draw = star(5,100)
    penup()
    forward(350)
    right(144)
    pendown()


mainloop()
