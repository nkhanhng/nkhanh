from turtle import *

bgcolor("lightgreen")
shape("turtle")
color("blue")
pensize(5)

for i in range(12):
    for j in range(1):
        penup()
        forward(100)
        pendown()
        for z in range(2):
            forward(20)
            penup()
        stamp()
    backward(140)
    right(30)

stamp()
mainloop()
