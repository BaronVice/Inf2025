def condition(p1, p2):
    maxx = max(p1, p2)
    minn = min(p1, p2)
    vanya = minn + maxx // 2
    return vanya <= 20


def game(p1, p2, turn):
    if turn == 0:
        if condition(p1 - 1, p2) and condition(p1, p2 - 1) and condition(p1 // 2, p2) and condition(p1, p2 // 2):
            return False

    if turn == 1:
        if p1 + p2 <= 20: return False
    if turn == 2:
        if p1 + p2 <= 20: return True
    if turn == 3:
        if p1 + p2 <= 20: return False
    if turn == 4:
        if p1 + p2 <= 20: return True
        else: return False

    if turn == 0:
        return game(p1 - 1, p2, turn+1) and game(p1, p2 - 1, turn+1) and game(p1 // 2, p2, turn+1) and game(p1, p2 // 2, turn+1)
    if turn == 1:
        return game(p1 - 1, p2, turn+1) or game(p1, p2 - 1, turn+1) or game(p1 // 2, p2, turn+1) or game(p1, p2 // 2, turn+1)
    if turn == 2:
        return game(p1 - 1, p2, turn+1) and game(p1, p2 - 1, turn+1) and game(p1 // 2, p2, turn+1) and game(p1, p2 // 2, turn+1)
    if turn == 3:
        return game(p1 - 1, p2, turn+1) or game(p1, p2 - 1, turn+1) or game(p1 // 2, p2, turn+1) or game(p1, p2 // 2, turn+1)

for i in range(11, 200):
    if game(10, i, 0):
        print(i)