# https://inf-ege.sdamgia.ru/problem?id=47210

from turtle import *

# Изначально черепаха смотрит вправо, повернем ее вверх (90 градусов влево)
left(90)
# Установим пиксели на единицу по координатам (20-30 достаточно)
scale=100

# При желании можно выставить размер окна: screensize(2000,2000)

# Если хочется посмотреть анимацию, то tracer(1) 
tracer(0)

# pendown() - опустить хвост (рисует при передвижении)
# При запуске хвост опущен, но пропишем все-равно это
pendown()
fillcolor("red")
begin_fill()
for i in range(4):
    forward(12*scale)
    right(90)
end_fill()

# Еще можно устанавливать цвет черепахи
color("green")
# И делать заливку фигур
fillcolor("green")
# Сперва нарисуем ограничивающую фигуру (точки внутри нее будем ичключать)
for i in range(3):
    # Начать покраску
    begin_fill()
    forward(8*scale)
    right(60)
    forward(8*scale)
    right(120)
    # Закончить покраску
    end_fill()

penup()

result = 0
sc = getcanvas()
for x in range(-100*scale, 100*scale, scale):
    for y in range(-100*scale, 100*scale, scale):
        item_ids = sc.find_overlapping(x,y,x,y)
        if len(item_ids) != 0 and sc.itemcget(item_ids[-1], 'fill')=='red': result += 1
print(result)
# Чтобы окно не закрывалось после выполнения:
done()