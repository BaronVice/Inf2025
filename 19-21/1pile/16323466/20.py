# https://inf-ege.sdamgia.ru/problem?id=27833

def game(amount, turn):
    if turn == 1:
        if (amount + 1 >= 52 or amount + 4 >= 52 or amount * 2 >= 52):
            return False
        turn += 1
        return game(amount + 1, turn) or game(amount + 4, turn) or game(amount * 2, turn)
    
    if turn == 2:
        if (amount + 1 >= 52 or amount + 4 >= 52 or amount * 2 >= 52):
            return False
        
        turn += 1
        return game(amount + 1, turn) and game(amount + 4, turn) and game(amount * 2, turn)
    
    if turn == 3:
        if (amount + 1 >= 52 or amount + 4 >= 52 or amount * 2 >= 52):
            return True
        else:
            return False
        
    # Количество кода можно сократить заметив, что turn % 2 == 1 -> ходит Петя, иначе ходит Ваня


for i in range(52):
    if game(i, 1):
        print(i)