
def game_f(n, t):
    if t == 1:
        if (n-2) // 3 <= 19 and (n-5) // 3 <= 19 and (n//3) // 3 <= 19: return False
    if t == 1 or t == 3:
        if n // 3 <= 19: return False
    if t == 2 or t == 4:
        if n // 3 <= 19: return True
    if t == 5: return False

    # Ваня
    if t % 2 == 0: return game_f(n-2, t+1) or game_f(n-5, t+1) or game_f(n//3, t+1)
    # Петя
    else: return game_f(n-2, t+1) and game_f(n-5, t+1) and game_f(n//3, t+1)

for i in range(20, 250):
    if game_f(i, 1) == 1:
        print(i)
        break