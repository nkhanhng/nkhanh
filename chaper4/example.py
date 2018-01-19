import turtle

wn = turtle.Screen()

tess = turtle.Turtle()
tess.shape("turtle")

def draw_rectangle(t,w,h):
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)

def draw_square(tx, sz):
    draw_rectangle(tx, sz, sz)

size = 100
for i in range(2):
    draw_square(tess, size)

wn.mainloop()
