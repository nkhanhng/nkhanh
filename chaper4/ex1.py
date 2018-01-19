import turtle

def make_window(colr,ttle):
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

def draw_rectangle(t,w,h):
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)

def draw_square(tx, sz):
    draw_rectangle(tx, sz, sz)

wn = turtle.Screen()

tess = turtle.Turtle()
tess.shape("turtle")
tess.speed(1)
size = 20
for j in range(5):
    for i in range(2):
        draw_square(tess,size)
    tess.penup()
    tess.forward(40)
    tess.pendown()

wn.mainloop()
