# https://inf-ege.sdamgia.ru/problem?id=27816

def game(amount, turn):
    # По условию "у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом"
    if turn == 1:
        # Проверить это можно так: ход Пети, чтобы количество камней в кучках было минимальным +1
        # ход Вани, который его больше всего приблизит к выигрышу *5
        # Если Ваня таким образом получит 70 камней, то он гарантировано выигрывает первым ходом
        if (amount + 1) * 5 >= 70:
            return False
    if turn == 2 and (amount + 1 >= 70 or amount + 4 >= 70 or amount * 5 >= 70):
        # Ваня побеждает первым ходом
        return True
    if turn == 3 and (amount + 1 >= 70 or amount + 4 >= 70 or amount * 5 >= 70):
        # Петя побеждает вторым ходом
        return False
    if turn == 4 and (amount + 1 >= 70 or amount + 4 >= 70 or amount * 5 >= 70):
        # Ваня побеждает вторым ходом
        return True
    if turn == 5:
        # Ваня не может победить вторым ходом
        return False
    

    # Если ходит Ваня - один из его ходов (or) должен привести его к победе
    # Спрева проверим кто ходит
    if turn % 2 == 0:
        # Затем передадим ход
        turn += 1
        return game(amount + 1, turn) or game(amount + 4, turn) or game(amount * 5, turn)
    # Если ходит Петя - любой его ход (and) должен привести его к поражению
    else:
        turn += 1
        return game(amount + 1, turn) and game(amount + 4, turn) and game(amount * 5, turn)


for i in range(100):
    # i - исходное количество камней (S), 1 - первый ход Пети
    if game(i, 1):
        print(i)
        break