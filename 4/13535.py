# https://inf-ege.sdamgia.ru/problem?id=13535

"""
По каналу связи передаются сообщения, содержащие только шесть букв: А, B, C, D, E, F.
Для передачи используется неравномерный двоичный код, удовлетворяющий условию Фано.
Для букв A, B, C используются такие кодовые слова: А — 11, B — 101, C — 0.

Укажите кодовое слово наименьшей возможной длины, которое можно использовать для буквы F.
Если таких слов несколько, укажите то из них,
которое соответствует наименьшему возможномудвоичному числу. 

Условие Фано означает, что ни одно кодовое слово не является началом другого кодового слова.
"""

# Является ли слово b началом слова a
# a = "1111"
# b = "11"
# print(a.startswith(b)) -> True

# Каждый раз подбирая слово будем проверять, 
# что оно не является началом других и другие не являются его началом

# В задании известны коды трех букв и еще три надо подобрать
a = "11"
b = "101"
c = "0"

# Нагенерируем различные коды длины 6 (их должно быть достаточно для подбора трех под условие Фано)
generated = []
for i1 in "01":
    generated.append(i1)
    for i2 in "01":
        generated.append(i1+i2)
        for i3 in "01":
            generated.append(i1+i2+i3)
            for i4 in "01":
                generated.append(i1+i2+i3+i4)
                for i5 in "01":
                    generated.append(i1+i2+i3+i4+i5)
                    for i6 in "01":
                        generated.append(i1+i2+i3+i4+i5+i6)
# Можно посортировать, а можно и нет
generated.sort(key=len)
# print(generated)

n = len(generated)
answer = "------------"
# Затем будем подбирать тройки d,e,f
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            d = generated[i]
            e = generated[j]
            f = generated[k]
            picked = [a,b,c,d,e,f]
            good = True
            # И проверять, соответствуют ли они условию Фано
            for w1 in range(6):
                for w2 in range(w1+1, 6):
                    # Если хотя бы одна пара w1,w2 из a,b,c,d,e,f получает True
                    if picked[w1].startswith(picked[w2]) or picked[w2].startswith(picked[w1]):
                        # То условие Фано не выполняется
                        good = False
                        break
            # А иначе нашли тройку чисел, соответствующих условию
            if good:
                # Если пара подходит, то выбираем элемент минимальный по длине
                minn = min(answer, d, e, f, key=len)
                # Если длина разная, то берем наименьшее по длине
                if len(answer) != len(minn): answer = minn
                # Иначе берем наименьшее числовое значение
                else: answer = min(answer, minn)
print(answer)


