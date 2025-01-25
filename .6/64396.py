from turtle import *

tracer(0)
left(90)
k = 25

for i in range(4):
    for j in range(4):
        forward(8*k)
        right(90)
    forward(13*k)
    right(90)
    forward(4*k)

teleport(0,0)
for x in range(-5, 20):
    for y in range(-5, 20):
        teleport(x * k, y * k)
        dot(4, "red")

done()
