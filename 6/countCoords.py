from turtle import *

# Разберем алгоритм, который посчитает количество точек за нас

# Пусть есть фигура (в данном примере квадрат) с карсной заливкой
# Тогда построив фигуру посчитаем количество координат для которых плоскость красная  

speed(0)
color("black", "red") # черная линия, заливка красная
k = 25 # 25 пикселей на единицу
begin_fill()

seth(90) # повернем вверх
for i in range(4):
    forward(6 * k)
    right(90)
end_fill()

# Для начала получим элемент черепашки канвас (то, на чем рисовали)
sc = getcanvas()
# Спрячем черепашку, чтобы она не нарушала подсчет точек (она тоже элемент канваса)
hideturtle()

result = 0
# Переберем все точки (x и y от -100 до 100 должно хватить)
for x in range(-100*k, 100*k, k):
    for y in range(-100*k, 100*k, k):
        # sc.find_overlaping(x1,y1,x2,y2) вернет список из элементов канваса,
        # которые входят в прямоугольник,
        # левый верхний угол которого имеет координаты x1 y1,
        # правый нижний угол которого имеет координаты x2 y2

        # Однако нам нужно получить элемент в точке, поэтому запись будет sc.find_overlapping(x,y,x,y)
        item_ids = sc.find_overlapping(x,y,x,y)
        # В точке нет фигуры - len(item_ids) == 0, иначе фигура есть
        # Фигура состоит из двух элементов: линия и заливка. 
        # Поэтому в item_ids будет или линия (она черная) или заливка (она красная).
        # Берем элемент и проверяем его цвет.
        if len(item_ids) == 1 and sc.itemcget(item_ids[0], 'fill')=='red': result += 1

print(result)
done()