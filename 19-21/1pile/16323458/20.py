# https://inf-ege.sdamgia.ru/problem?id=27815

def game(amount, turn):
    # По условию "Петя не может выиграть за один ход"
    if turn == 1 and (amount + 1 >= 70 or amount + 4 >= 70 or amount * 5 >= 70):
        return False
    if turn == 2 and (amount + 1 >= 70 or amount + 4 >= 70 or amount * 5 >= 70):
        # Ваня побеждает первым ходом
        return False
    if turn == 3 and (amount + 1 >= 70 or amount + 4 >= 70 or amount * 5 >= 70):
        # Петя побеждает вторым ходом
        return True
    if turn == 4:
        # Петя не может победить вторым ходом
        return False
    

    # Если ходит Петя - один из его ходов (or) должен привести его к победе
    # Спрева проверим кто ходит
    if turn % 2 == 1:
        # Затем передадим ход
        turn += 1
        return game(amount + 1, turn) or game(amount + 4, turn) or game(amount * 5, turn)
    # Если ходит Ваня - любой его ход (and) должен привести его к поражению
    else:
        turn += 1
        return game(amount + 1, turn) and game(amount + 4, turn) and game(amount * 5, turn)


for i in range(100):
    # i - исходное количество камней (S), 1 - первый ход Пети
    if game(i, 1):
        print(i)