import turtle

wn = turtle.Screen()
def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(45)
        
def draw_equitriangle(tx,s):
    draw_poly(tx,3,s)
    tx.left(15)

tess = turtle.Turtle()
tess.shape("turtle")
tess.pensize(1)
tess.speed(0)

draw_equitriangle(tess,100)

wn.mainloop()
