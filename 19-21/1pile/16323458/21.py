def game_f(n, t):
    if t == 1:
        if (n+1) * 5 >= 70 and (n + 4) * 5 >= 70 and (n*5) * 5 >= 70: return False
    if t == 1 or t == 3:
        if n * 5 >= 70: return False
    if t == 2:
        if n * 5 >= 70: return True
    if t == 4:
        if n * 5 >= 70:
            return True
        else:
            return False

    if t % 2 == 0:
        return game_f(n + 1, t + 1) or game_f(n + 4, t + 1) or game_f(n * 5, t + 1)
    else:
        return game_f(n + 1, t + 1) and game_f(n + 4, t + 1) and game_f(n * 5, t + 1)


for i in range(1, 70):
    if game_f(i, 1) == 1:
        print(i)