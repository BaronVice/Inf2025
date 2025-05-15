# https://inf-ege.sdamgia.ru/problem?id=47403

from turtle import *

speed(0)

seth(90)

forward(100)
left(90) # right(90)
backward(100)

up()
backward(100)

down()
seth(270)
color("red")
forward(100)

up()
for x in range(0, 100 + 1, 10):
    for y in range(0, 100 + 1, 10):
        goto(x,y)
        dot(5)

done()
