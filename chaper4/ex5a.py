import turtle

def make_window(colr,ttle):
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

wn = make_window("lightgreen","ex5a")

def draw_something(t, n, sz):
    for i in range(n):
        t.right(90)
        t.forward(sz)
        sz += 10

tess = turtle.Turtle()
tess.shape("turtle")
tess.pensize(5)
tess.speed(1)

draw_something(tess, 20, 1)

wn.mainloop()
