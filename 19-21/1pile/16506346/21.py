def check(s):
    return s * 3 >= 64

def game(s, t):
    if t % 2 == 1:
        # Вышли в третий ход -> False
        if t == 5:
            return False
        # Первый ход Пети
        if t == 1:
            # Оба хода Пети приводят его к поражению -> False
            if check(s+1) and check(s*3): return False

        # Выигрывает Петя -> False
        if s * 3 >= 64:
            return False
        
        t += 1
        # Из обоих ходов Пети Ваня должен выиграть
        return game(s+1, t) and game(s*3, t)
    else:
        # Ваня выигрывает
        if s * 3 >= 64:
            return True

        t += 1
        # Хотя бы один ход Вани должен привести его к победе
        return game(s+1, t) or game(s*3, t)
    

for i in range(1, 64):
    if game(i, 1):
        print(i)