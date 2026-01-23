
"""
На числовой прямой даны два отрезка: P = [25; 64] и Q = [40; 115].
Укажите наименьшую возможную длину такого отрезка A, что логическое выражение
(x ∈ P) → (((x ∈ Q) /\ ¬ (x ∈ A)) → ¬ (x ∈ P))
истинно (т.е. принимает значение 1) при любом значении переменной х.
"""

min_len = 10**9
# Перебор
for a_start in range(0, 200):
    for a_end in range(200, 0, -1):

        if a_start > a_end:
            continue

        fl = True
        for x in range(0, 200):
            # (x ∈ P) → (((x ∈ Q) /\ ¬ (x ∈ A)) → ¬ (x ∈ P))
            if not (25 <= x <= 64) <= (((40 <= x <= 115) and (not(a_start <= x <= a_end))) <= (not(25 <= x <= 64))):
                fl = False
                break
        
        if fl:
            min_len = min(min_len, a_end-a_start)

print(min_len) # 24