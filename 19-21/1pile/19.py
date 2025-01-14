# 0 - 1-ый Пети
# 1 - 1-ый Вани
# 2 - 2-ой Пети
# 3 - 2-ой Вани


def game(s, turn):
    if turn == 2 and s >= 45: return True
    if turn == 2 and s < 45: return False

    if turn == 0:
        return game(s + 1, turn + 1) or game(s * 2, turn + 1)
    if turn == 1:
        return game(s + 1, turn + 1) or game(s * 2, turn + 1)


for i in range(1, 45 + 1):
    if game(i, 0):
        print(i)
        break