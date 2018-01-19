import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Hello, Tess!")

tess = turtle.Turtle()
col = input("Which color do you want to set?")
tess.color(col)
ps = int(input("Which size of pen do you to set?"))
tess.pensize(ps)

alex = turtle.Turtle()

for c in ["red","blue"]:
    tess.color(c)
    tess.forward(100)
    tess.left(120)

for i in range (3):
    alex.forward(200)

wn.mainloop()
