# https://inf-ege.sdamgia.ru/problem?id=58486

# Заметим, что операция *2 к одной из кучек применима, только если a1 != a2
def game(a1, a2, t):
    a1, a2 = max(a1, a2), min(a1, a2)
    if a1 == a2:
        return a1 + 3 >= 48
    
    # Варианты с +1 и +2 можно не рассматривать, поскольку достаточно +3
    return a1 + 3 >= 48 or a2 * 2 >= 48

ans = 10**9
for i in range(1,48):
    for j in range(1,48):
        if game(i, j, 1):
            ans = min(ans, i + j)
print(ans)