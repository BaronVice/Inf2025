# https://inf-ege.sdamgia.ru/problem?id=58487

def game(a1, a2, t):
    a1, a2 = max(a1, a2), min(a1, a2)

    if t % 2 == 1:
        # Проверим, что Петя не может выиграть первым ходом
        if t == 1:
            if a1 == a2 and a1 + 3 >= 48: return False
            if a1 + 3 >= 48 or a2 * 2 >= 48: return False
            # На самом деле эти два if можно заменить на один, проверяя возможность *2 при разном количестве камней в кучах
            # if a1 + 3 >= 48 or (a1 != a2 and a2 * 2 >= 48): return False

        # Если это второй ход Пети, то он должен выиграть
        if t == 3: return a1 + 3 >= 48 or (a1 != a2 and a2 * 2 >= 48)

        t += 1
        return (game(a1 + 1, a2, t) or game(a1 + 2, a2, t) or game(a1 + 3, a2, t)
                    or (a1 != a2 and game(a1, a2 * 2, t)))
    else:
        # Проверим что Ваня не выигрывает
        if a1 + 3 >= 48 or (a1 != a2 and a2 * 2 >= 48): return False
        t += 1
        # Все ходы Вани должны привести его к поражению (ВАЖНО: если a1 == a2, то game(a1, a2 * 2, t) надо пропустить)
        return (game(a1 + 1, a2, t) and game(a1 + 2, a2, t) and game(a1 + 3, a2, t)
                    # Если a1 == a2, то у Вани нет возможности использовать *2 -> результат True, иначе запускаем game(a1, a2 * 2, t)
                    and (a1 == a2 or game(a1, a2 * 2, t)))


for j in range(1,48):
    if game(13, j, 1):
        print(j)