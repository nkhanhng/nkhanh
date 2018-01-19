import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
alex.shape("square")
alex.speed(1)

for i in ["yellow","red","purple","blue"]:
    alex.color(i)
    alex.forward(200)
    alex.left(90)

wn.mainloop()
