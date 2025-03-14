

def game(n, t):
    if t == 0:
        if n * 2 >= 31: return False
    if t == 1:
        if n * 2 >= 31: return False
    if t == 2:
        if n * 2 >= 31: return True
        else: return False

    if t % 2 == 0:
        return game(n + 1, t + 1) or game(n + 2, t + 1) or game(n * 2, t + 1)
    else:
        return game(n + 1, t + 1) and game(n + 2, t + 1) and game(n * 2, t + 1)


for s in range(1, 30 + 1):
    if game(s, 0):
        print(s)

