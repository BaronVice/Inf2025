

def game(s1, s2, t):
    if t == 5: return False
    if t == 1:
        if (s+1) * 3 >= 38 and (s*3) * 3 >= 38: return False

    # Ваня
    if t % 2 == 0:
        if s * 3 >= 38: return True
        return game(s+1, t+1) or game(s*3, t+1)
    # Петя
    else:
        if s * 3 >= 38: return False
        return game(s+1, t+1) and game(s*3, t+1)


for i in range(38):
    if game(i, 7, 1):
        print(i)
        break