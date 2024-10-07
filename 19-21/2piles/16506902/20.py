def c(i, j):
    return max(i, j) + i + j >= 67


def game(i, j, t):
    # "Ваня не может гарантировано выиграть первым ходом"
    if t == 1 and c(i + 1, j) and c(i, j + 1) and c(i + j, j) and c(i, j + i): return False

    # Петя выигрывает -> False
    if (t == 1 or t == 3) and max(i, j) + i + j >= 67: return False
    # Ваня может выиграть первым или вторым ходом?
    if (t == 2 or t == 4) and max(i, j) + i + j >= 67: return True
    
    # Зашли в третий ход -> False
    if t == 5: return False

    # Ходит Ваня
    if t % 2 == 0:
        t += 1
        # Хотя бы один из ходов Вани должен привести его к победе
        return game(i + 1, j, t) or game(i, j + 1, t) or game(i + j, j, t) or game(i, j + i, t)
    # Ходит Петя
    else:
        t += 1
        # Из всех ходов Пети Ваня должен победить
        return game(i + 1, j, t) and game(i, j + 1, t) and game(i + j, j, t) and game(i, j + i, t)


for i in range(1, 57):
    if game(9, i, 1):
        print(i) 
