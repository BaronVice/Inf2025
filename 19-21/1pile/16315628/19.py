# https://inf-ege.sdamgia.ru/problem?id=70546

def game(p1, turn):
    if turn == 0:
        if p1 // 3 <= 19: return False
    if turn == 1:
        if p1 // 3 <= 19: return True
        else: return False

    if turn == 0:
        return game(p1-2, turn+1) and game(p1-5, turn+1) and game(p1//3, turn+1)


for i in range(20, 200):
    if game(i, 0):
        print(i)
        break
