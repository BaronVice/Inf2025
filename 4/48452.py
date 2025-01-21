from itertools import *

# Нагенерируем различные коды длины от 1 до 6 (их должно быть достаточно для подбора трех под условие Фано)
generated = []
for i in range(1, 5):
    p = product("01", repeat = i) # генерация tuple-ов длины i из элементов 0 и 1
    for result in p:
        generated.append( "".join(result) ) # из tuple в строку

# Комбинации троек из generated
cmbs = list(combinations(generated, 3))
for c in cmbs:
    # В задании известны коды трех букв и еще три надо подобрать
    picked = ["000", "11", "100", c[0], c[1], c[2]]
    # Для каждой пары слов проверим, что одно не является началом второго
    pairs = combinations(picked, 2) # комбинации из picked длины 2
    # Проверка всех пар на выполнение условия Фано
    is_good = all(
        [0 if pair[0].startswith(pair[1]) or pair[1].startswith(pair[0]) else 1 for pair in pairs]
    )
    if is_good:
        # Если пара подходит, то выбираем элемент минимальный по длине
        print(c[0], c[1], c[2])