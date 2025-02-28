# 0 - 1-ый Пети
# 1 - 1-ый Вани
# 2 - 2-ой Пети
# 3 - 2-ой Вани


def game(n, turn):
    if turn == 0:
        if n * 5 >= 70: return False
    if turn == 1:
        return n * 5 >= 70
    
    if turn == 0 or turn == 2:
        return game(n + 1, turn+1) or game(n + 4, turn+1) or game(n * 5, turn+1)
    else:
        return game(n + 1, turn+1) or game(n + 4, turn+1) or game(n * 5, turn+1)


for i in range(1, 69 + 1):
    if game(i, 0):
        print(i)
        break
