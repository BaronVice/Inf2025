# https://inf-ege.sdamgia.ru/problem?id=47245

from turtle import *
left(90)
k = 25
hideturtle()

pendown()
speed(0)
fillcolor("red")
begin_fill()
for i in range(3):
    forward(9*k)
    right(120)
end_fill()

sc = getcanvas()
result = 0
for x in range(-100*k, 100*k, k):
    for y in range(-100*k, 100*k, k):
        item_ids = sc.find_overlapping(x,y,x,y)
        if len(item_ids) != 0 and sc.itemcget(item_ids[-1], 'fill')=='red': result += 1

print(result)
done()
