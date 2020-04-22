import turtle as t

t.setup(1200,700)
t.penup()
t.goto(-500,300)
t.pensize(5)
t.pendown()


def kangtuoer(size,n):
    if n==0:
        t.fd(size)
    else:
        kangtuoer(size/3,n-1)
        t.penup()
        kangtuoer(size/3,0)
        t.pendown()
        kangtuoer(size/3,n-1)
        
level=6
color=['red','yellow','green','blue','black','purple']
for i in range(level):
    t.pencolor(color[i])
    kangtuoer(1000,i)
    t.penup()
    t.goto(-500,200-i*100)
    t.pendown()

t.hideturtle()
t.done()
