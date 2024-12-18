# https://inf-ege.sdamgia.ru/problem?id=27538

"""
Для проведения эксперимента записывается звуковой фрагмент в формате квадро (четырёхканальная запись)
с частотой дискретизации 32 кГц и 32-⁠битным разрешением.
Результаты записываются в файл, сжатие данных не производится;
дополнительно в файл записывается служебная информация, необходимая для эксперимента,
размер полученного файла 97 Мбайт.

Затем производится повторная запись этого же фрагмента в формате моно (одноканальная запись)
с частотой дискретизации 16 кГц и 16-⁠битным разрешением.
Результаты тоже записываются в файл без сжатия и со служебной информацией,
размер полученного файла 7 Мбайт.

Объём служебной информации в обоих случаях одинаков.
Укажите этот объём в мегабайтах.
В ответе укажите только число (количество Мбайт), единицу измерения указывать не надо.
"""

"""
V = t * u * ch * i + a
V - объем памяти для хранения звукозаписи в битах,
t - время звукозаписи
u - частота дискретизации
ch - количество каналов записи
i - разрешение записи
a - размер служебной информации

- Поскольку музыкальный фрагмент не менялся, то и время звукозаписи не менялось
- Размер служебной информации тоже не менялся
1) Для первой звукозаписи:
V1 = 97 Мбайт = 97 * 1024 * 1024 * 8 бит
t = t
u = 32000
ch = 4
i = 32
a = a

2) Для второй звукозаписи:
V2 = 7 Мбайт = 7 * 1024 * 1024 * 8 бит
t = t
u = 16000
ch = 1
i = 16
a = a

V1 = 97 * 1024 * 1024 * 8 = t * 32000 * 4 * 32 + a
V2 = 7 * 1024 * 1024 * 8 = t * 16000 * 1 * 16 + a

Получаем два уравнения. Решается такое через объединение их в систему.
Проще всего будет вынести a из первого, подставить во второе, получить t.
V1:
97 * 1024 * 1024 * 8 = t * 32000 * 4 * 32 + a
a = 97 * 1024 * 1024 * 8 - t * 32000 * 4 * 32

Подставим во второе
V2:
7 * 1024 * 1024 * 8 = t * 16000 * 1 * 16 + a
7 * 1024 * 1024 * 8 = t * 16000 * 1 * 16 + 97 * 1024 * 1024 * 8 - t * 32000 * 4 * 32
# Через python можно подобрать t написав перебор.
7 * (1024 * 1024 * 8) - 97 * (1024 * 1024 * 8) = t * (16000 * 16) - t * (32000 * 4 * 32)
-90 * (1024 * 1024 * 8) = t * (16000 * 16 - 32000 * 4 * 32)
-754974720 = -3840000 * t
t = 196.608
- Подставляем t в любое из уравнений (я подставлю в первое)
97 * 1024 * 1024 * 8 = 196.608 * 32000 * 4 * 32 + a
a = 97 * 1024 * 1024 * 8 - 196.608 * 32000 * 4 * 32 = 8388608 (это в битах)
a в Мбайт = 8388608 / 8 / 1024 / 1024 = 1

- Примечание: эту систему уравнений можно было решить намного элегантнее используя свертку в степени двоек.

Ответ: 1
"""
