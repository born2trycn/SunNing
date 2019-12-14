import turtle
import time


a = turtle.Pen()
a.shape('turtle')
a.hideturtle()

now = time.gmtime()
print(now)

month = now.tm_mon
day = now.tm_mday

print(month)
print(day)

if (month == 9 and day == 10):
    a.write('❤❤❤❤❤❤❤', font=('Arial', 20, 'normal'))
a.speed(100)
a.forward(200)
a.left(90)
a.forward(50)
a.left(90)
a.forward(200)
a.left(90)
a.forward(50)
a.left(180)
a.forward(50)
a.right(90)
a.forward(50)
a.left(90)
a.forward(50)
a.right(90)
a.forward(100)
a.right(90)
a.forward(50)
a.left(180)
a.forward(50)
a.left(90)
a.forward(10)
a.right(90)
a.forward(50)
a.left(90)
a.forward(10)
a.left(90)
a.forward(50)
a.right(90)
a.forward(20)
a.right(90)
a.forward(50)
a.left(90)
a.forward(10)
a.left(90)
a.forward(50)
a.right(90)
a.forward(20)
a.right(90)
a.forward(50)
a.left(90)
a.forward(10)
a.left(90)
a.forward(50)
a.hideturtle()
turtle.done()


if (month == 4 and day == 24):
    a.write('今天是妈妈的生日呀')

if (month == 12 and day == 9):
    a.write('今天是爸爸的生日呀')

if (month == 6 and day == 21):
    a.write('今天父亲节 嗷~~')

if (month == 5 and day == 10):
    a.write('今天母亲节 嗷~~')
