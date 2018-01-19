import turtle
wn = turtle.Screen()

tess = turtle.Turtle()
tess.shape("turtle")
tess.color("red")
tess.speed(1)

tess.penup()
size = 20
for i in range(20):
    tess.stamp()
    size = size + 3
    tess.forward(size)
    tess.left(24)

# tess.color("blue")


wn.mainloop()
