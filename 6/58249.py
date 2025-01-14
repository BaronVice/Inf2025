from turtle import *
hideturtle()
k = 25
penup()
left(90)
pendown()
fillcolor("pink")
begin_fill()
for i in range(1):
    seth(180)
    circle(-5 * k, 180)
    seth(90)
    circle(-5 * k, 180)
    seth(0)
    circle(-5 * k, 180)
    seth(270)
    circle(-5 * k, 180)
end_fill()
ans = 0
sc = getcanvas()
for x in range(-100 * k, 100 * k, k):
    for y in range(-100 * k, 100 * k, k):
        i = sc.find_overlapping(x, y, x, y)
        if len(i) != 0 and sc.itemcget(i[-1], 'fill') == "pink": ans += 1
print(ans)