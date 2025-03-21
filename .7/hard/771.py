# 771 из https://kompege.ru/task

"""
20 изображений разрешением 1600х1200 пикселей отправили по каналу связи со средней пропускной способностью 2**23 бит/секунду.
Все изображения были приняты приемником не более, чем 10 секунд.

Известно, что изображение кодируется, как набор пикселей,
каждый из которых закодирован с помощью одинакового и минимально возможного количества бит.
Изображения в целях ускорения передачи записаны в памяти подряд, без разделителей и заголовков.

Какое максимальное число цветов может быть в палитре?
"""

"""
Сколько памяти занимает одна фотография:
V = h * w * i, где h * w - размер фотографии, i - глубина цвета.
Глубина цвета неизвестна. По заданию она нужна, чтобы найти максимальное число цветов (N = 2**i).

n изображений, занимающих V бит, будут передаваться t секунд со скорость q:
t = n*V / q
10 = 20*(1600 * 1200 * i) / 2**23
10 = 20 * 1600 * 1200 * i / 2**23
10 * 2**23 / 20 / 1600 / 1200 = i
i = 2.1845

Все изображения были приняты приемником не более, чем 10 секунд -> округляем i до меньшего целого.
i = 2, N = 2**i = 2**2 = 4
Ответ: 4
"""
