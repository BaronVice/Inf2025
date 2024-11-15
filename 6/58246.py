# https://inf-ege.sdamgia.ru/problem?id=58246

from turtle import *

scale = 30
color('black','red')
hideturtle()
speed(0)

begin_fill()

# seth: черепашка смотрит
# 0 - вправо
# 90 - вверх
# 180 - влево
# 270 - вниз
seth(90)
right(180)
forward(5*scale)
right(90)
forward(50*scale)
right(90)
forward(5*scale)
for i in range(5):
    seth(90)
    # circle(right, rads) - нарисовавть окружность в rads радиан, 
    # с центром справа от черепашки на right пикселей 
    circle(-5*scale, 180)
end_fill()

result = 0
sc = getcanvas()
for x in range(-100*scale, 100*scale, scale):
    for y in range(-100*scale, 100*scale, scale):
        item_ids = sc.find_overlapping(x,y,x,y)
        if len(item_ids) != 0 and sc.itemcget(item_ids[-1], 'fill')=='red': result += 1

print(result)
done()