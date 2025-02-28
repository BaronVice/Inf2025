from turtle import *
k = 5
goto(-150*k, 0)
fillcolor("pink")
for i in range(20):
    circle(4*k)
    goto(8*k + xcor(), ycor())
goto(xcor(), ycor() - 12*k)
for i in range(10):
    circle(8*k)
    goto(-16*k + xcor(), ycor())
goto(xcor(), ycor() - 14*k)
for i in range(15):
    circle(6*k)
    goto(12*k + xcor(), ycor())
done()
'''
sc = getcanvas()
ans = 0
for x in range(-100*k, 100*k, k):
    for y in range(-100*k, 100*k, k):
        ii = sc.find_overlapping(x, y, x, y)
        if len(ii) > 0 and sc.itemcget(ii[-1], 'fill') == "pink": ans += 1
print(ans)
'''