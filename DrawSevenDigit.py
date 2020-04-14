import turtle as t

#加点空隙
def gap():
    t.penup()
    t.fd(5)

#绘制一条线
def drawline(line):
    gap()
    t.pendown() if line else t.penup()
    # t.pendown() if line == True else t.penup()
    t.fd(40)
    gap()
    t.right(90)


#绘制一个数字
def drawdigit(num):
    drawline(True) if num in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if num in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if num in [2,3,0,5,6,8,9] else drawline(False)
    drawline(True) if num in [2,0,6,8] else drawline(False)
    t.left(90)
    drawline(True) if num in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if num in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if num in [0,2,3,4,1,7,8,9] else drawline(False)
    t.penup()
    t.right(180)
    t.fd(40)

#封装一下日期的循环
def drawdate(date):
    for i in date:
        drawdigit(eval(i))

#主程序
def main():
    t.setup(1000,600)
    t.penup()
    t.fd(-300)
    t.pencolor('red')
    t.pensize(5)
    drawdate('12345678')
    t.hideturtle()  
    t.done()

main()