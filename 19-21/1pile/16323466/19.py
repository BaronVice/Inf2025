# https://inf-ege.sdamgia.ru/problem?id=27832

def game(amount, turn):
    if turn == 1:
        turn += 1
        return game(amount + 4, turn) or game(amount * 2, turn)
    if turn == 2:
        return (amount + 4 >= 52 or amount * 2 >= 52)


for i in range(52):
    if game(i, 1):
        print(i)
        break