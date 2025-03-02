# https://inf-ege.sdamgia.ru/problem?id=35465

"""
В информационной системе хранятся изображения размером 1024 x 768 пикселей.
Методы сжатия изображений не используются.
Каждое изображение дополняется служебной информацией, которая занимает 1280 Кбайт.
Для хранения 2048 изображений потребовалось 4 Гбайт.

Сколько цветов использовано в палитре каждого изображения?
"""

"""
I = K * i
N = 2**i
I - объем памяти для хранения изображения в битах,
K - количество пикселей,
i - количество памяти в битах, требуемое для хранения цвета
N - количество цветов.

* Заметим, что к каждому изображению добавляется информация 1280 Кбайт.
Тогда I = 1280 Кбайт + K * i, причем K нам известно -> I = 1280 Кбайт + 1024 * 768 * i

* Известно, что для 2048 изображений потребовалось 4 Гбайт.
* Тогда на одно изображение выделяется 4Гбайт/2048 (это будет I)
4 Гбайт / 2048 = I = 1280 Кбайт + 1024 * 768 * i
* Переведем все в биты
- Гбайт = 1024 Мбайт = 1024 * 1024 Кбайт = 1024 * 1024 * 1024 байт = 1024**3 * 8 бит
4 * 1024**3 * 8 / 2048 = 1280 * 1024 * 8 + 1024 * 768 * i     # Поделим обе части на 1024 * 8
4 * 1024 * 1024 / 2048 = 1280 + 96 * i
2 * 1024 = 1280 + 96 * i
2048 = 1280 + 96 * i
2048 - 1280 = 96 * i
(2048 - 1280) / 96 = i
i = 8

В задании просят найти количество цветов. N = 2**i = 2**8 = 256.
Ответ: 256
"""
