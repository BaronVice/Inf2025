from turtle import *
k = 100; speed(0); color('black','red'); hideturtle(); begin_fill()
seth(90); right(180); fd(2*k); right(90); fd(40*k); right(90); fd(2*k)
for i in range(4):seth(90); circle(-5*k,180)
end_fill(); sc = getcanvas()
otv = ['in' if (h:=sc.find_overlapping(x,y,x,y)) and sc.itemcget(h[-1],'fill')=='red' else 0\
       for x in range(-100*k,100*k,k) for y in range(-100*k,100*k,k)]
print(otv.count('in'))