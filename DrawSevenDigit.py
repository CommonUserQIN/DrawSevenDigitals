import turtle as t

#绘制一条线
def drawline(line):
    t.pendown() if line == True else t.penup()
    t.fd(40)
    t.right(90)


#绘制一个数字
def drawdigital(date):
    drawline(True) if date in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if date in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if date in [2,3,0,5,6,8,9] else drawline(False)
    drawline(True) if date in [2,0,6,8] else drawline(False)
    t.left(90)
    drawline(True) if date in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if date in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if date in [0,2,3,4,1,7,8,9] else drawline(False)


#主程序

date='23456789'
t.setup(800,600)
t.penup()
t.fd(-300)
t.pencolor('red')
t.pensize(5)
for i in date:
    drawdigital(eval(i))
    t.penup()
    t.right(180)
    t.fd(40)
t.done()