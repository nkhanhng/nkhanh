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

def jump_to_next_square(t,f):
    t.right(135)
    t.forward(f)
    t.left(135)

wn = make_window("lightgreen","innersquare")

tess = turtle.Turtle()
tess.shape("turtle")
tess.speed(5)
size = 20

for i in range(5):
    for j in range(2):
        draw_square(tess, size)
    tess.penup()
    jump_to_next_square(tess, 14)
    size += 20
    tess.pendown()


wn.mainloop()
