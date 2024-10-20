from turtle import *

k = 20
tracer(1)
color("black")
fillcolor("red")

begin_fill()
for i in range(5):
    # Помимо поворачивания черепашки через left() и rigth()
    # Ее можно направлять через seth() в определенном направлении
    # 0 - восток, 90 - север, 180 - запад, 270 - юг
    seth(0)
    circle(5*k, 180)
    seth(90)
    circle(5*k, 180)
    seth(180)
    circle(5*k, 180)
    seth(270)
    circle(5*k, 180)
end_fill()

# 
sc = getcanvas()
result = 0
for x in range(-100*k, 100*k, k):
    for y in range(-100*k, 100*k, k):
        item_ids = sc.find_overlapping(x,y,x,y)
        if len(item_ids) != 0 and sc.itemcget(item_ids[-1], 'fill')=='red': result += 1

print(result)

done()