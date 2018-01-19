import turtle

def make_window(colr,ttle):
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

def make_turtle(colr,sz,go):
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    t.forward(go)
    return t

wn = make_window("red","Tes and Alex")
tes = make_turtle("hotpink", 5,-100)
alex = make_turtle("blue", 9, 300)

wn.mainloop()
