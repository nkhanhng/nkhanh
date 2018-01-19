import turtle

def make_window(colr,ttle):
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

wn = make_window("lightgreen", "ex3")

def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(45)

tess = turtle.Turtle()
tess.shape("turtle")
tess.pensize(5)
tess.speed(1)

draw_poly(tess, 8, 50)

wn.mainloop()
