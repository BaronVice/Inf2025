# https://inf-ege.sdamgia.ru/problem?id=58248

from turtle import *
k = 100
speed(0)
color('black','red')
hideturtle()
begin_fill()

seth(90)
right(180)
forward(2*k)
right(90)
forward(40*k)
right(90)
forward(2*k)
for i in range(4):
       seth(90)
       circle(-5*k,180)
end_fill()

sc = getcanvas()
result = 0
for x in range(-100*k, 100*k, k):
    for y in range(-100*k, 100*k, k):
        item_ids = sc.find_overlapping(x,y,x,y)
        if len(item_ids) != 0 and sc.itemcget(item_ids[-1], 'fill')=='red': result += 1

print(result)