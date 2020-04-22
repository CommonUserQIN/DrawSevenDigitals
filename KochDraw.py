import turtle as t

t.setup(800,800)
t.penup()
t.goto(-200,200)
t.pencolor('black')
t.pensize(5)
t.pendown()


def kock(size,n):
    if n==0:
        t.fd(size)
    else:
        for angle in [0,60,-120,60]:
            t.left(angle)
            kock(size/3,n-1)
level=3
for angle in range(3):
    kock(500,level)
    t.right(120)

t.hideturtle()
t.done()
