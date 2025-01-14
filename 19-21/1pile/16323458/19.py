# https://inf-ege.sdamgia.ru/problem?id=27814

def game(amount, turn):
    # turn == 2 - первый ход Вани
    if turn == 2 and (amount + 1 >= 70 or amount + 4 >= 70 or amount * 5 >= 70):
        # Ваня выигрывает
        return True
    if turn == 3:
        # Ваня не выигрывает своим первым ходом
        return False
    
    # Передаем ход
    turn += 1
    # !!! ВНИМАТЕЛЬНО ЧИТАЕМ ЗАДАНИЕ !!!
    # В задании не указано, что игроки играют оптимально
    # Это значит, что нам нужен хотя бы один вариант, при котором Ваня выиграет
    return game(amount + 1, turn) or game(amount + 4, turn) or game(amount * 5, turn)


for i in range(100):
    # i - исходное количество камней (S), 1 - первый ход Пети
    if game(i, 1):
        print(i)
        break