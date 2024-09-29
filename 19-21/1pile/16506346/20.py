def game(s, t):
    if t % 2 == 1:
        # Петя выигрывает вторым ходом?
        if t == 3:
            return s * 3 >= 64

        # Петя не выигрывает первым ходом
        if s * 3 >= 64:
            return False
        t += 1

        # Хотя бы один ход Пети должен привести его к победе
        return game(s+1, t) or game(s*3, t)
    else:
        # Ваня выигрывает -> False
        if s * 3 >= 64:
            return False
        t += 1
        # Из обоих ходов Вани Петя должен выиграть
        return game(s+1, t) and game(s*3, t)
    

for i in range(1, 64):
    if game(i, 1):
        print(i)