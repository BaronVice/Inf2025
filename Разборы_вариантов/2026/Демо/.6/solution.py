
from turtle import *

seth(90)
tracer(0)

scale = 15
for _ in range(2):
    forward(14 * scale)
    left(270)
    backward(12 * scale)
    right(90)
up()
forward(9 * scale)
right(90)
backward(7 * scale)
left(90)
down()
for _ in range(2):
    forward(13 * scale)
    right(90)
    forward(6 * scale)
    right(90)

up()
color("red")
for x in range(-20, 10 + 1):
    for y in range(-10, 30 + 1):
        goto(x * scale, y * scale)
        dot(3)

done()

# 
