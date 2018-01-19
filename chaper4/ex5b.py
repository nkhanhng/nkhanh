import turtle

def make_window(colr,ttle):
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

wn = make_window("lightgreen","ex5a")

def draw_something(t, a, n, sz):
    for i in range(n):
        t.right(a)
        t.forward(sz)
        a += 0.01
        sz += 2

tess = turtle.Turtle()
tess.shape("turtle")
tess.pensize(1)
tess.speed(0)

draw_something(tess, 90, 200, 1)

wn.mainloop()
