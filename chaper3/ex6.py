import turtle

wn = turtle.Screen()

t = turtle.Turtle()
t.shape("turtle")

for i in range(8):
    t.forward(100)
    t.left(45)

wn.mainloop()
