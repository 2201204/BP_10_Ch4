삼색원
import turtle
t=turtle.Turtle()
t.shape("turtle")
a=input("색상#1을 입력하시오.:")
b=input("색상#2를 입력하시오.:")
c=input("색상#3을 입력하시오.:")
t.fillcolor(a)
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.goto(100,0)
t.down()

t.fillcolor(b)
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.goto(200,0)
t.down()

t.fillcolor(c)
t.begin_fill()
t.circle(50)
t.end_fill()

좌표 리스트
import turtle
t=turtle.Turtle()
t.shape("turtle")
t.shape("turtle")
list=[]
a=int(input("x1:"))
list.append(a)
a=int(input("y1:"))
list.append(a)
a=int(input("x2:"))
list.append(a)
a=int(input("y2:"))
list.append(a)
a=int(input("x3:"))
list.append(a)
a=int(input("y3:"))
list.append(a)
t.goto(list[0],list[1])
t.goto(list[2],list[3])
t.goto(list[4],list[5])
