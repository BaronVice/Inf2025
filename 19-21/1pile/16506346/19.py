def game(s, t):
    if t % 2 == 1:
        # Петя выигрывает -> False
        if s * 3 >= 64:
            return False
        t += 1
        # Из обоих ходов Пети Ваня должен выиграть
        return game(s+1, t) and game(s*3, t)
    else:
        # Ваня выигрывает?
        return s * 3 >= 64
    

for i in range(1, 64):
    if game(i, 1):
        print(i)