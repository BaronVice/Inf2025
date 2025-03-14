# https://inf-ege.sdamgia.ru/problem?id=69904

f = open("Inf2025\\_26\\Про_места_в_театре\\2626.txt")
n, m, k = map(int, f.readline().split())

# Ключ - номер места, значение - в каких рядах номер места занят
occupied_to_rows = dict()
for _ in range(n):
    row, place = map(int, f.readline().split())
    if place not in occupied_to_rows: occupied_to_rows[place] = [row]
    else: occupied_to_rows[place].append(row)

ans_row = -1
ans_max_places = 0

for occupied in occupied_to_rows.values():
    # Добавим 0 и m+1 для определения промежутков в начале и конце
    # (от начала до первого занятого места, от последнего занятого места и до конца ряда)
    l = sorted(occupied + [0, m+1])
    for i in range(len(l)-1):
        # Количество свободных мест между двумя занятыми = l[i+1] - l[i] - 1
        # Одно из свободных надо занять: l[i+1] - l[i] - 1 - 1
        ans = l[i+1] - l[i] - 1 - 1
        # Если количество свободных мест больше чем ранее найденное
        if ans > ans_max_places:
            ans_max_places = ans
            # l[i+1] - занятый, тогда берем ряд перед ним: l[i+1] - 1
            ans_row = l[i+1] - 1
        # Если количество свободных мест равно ранее найденному, но номер ряда меньше чем ранее найденный
        if ans == ans_max_places and ans_row > l[i+1] - 1:
            # То берем меньший номер ряда (по заданию)
            ans_row = l[i+1] - 1

print("Номер ряда", ans_row)
print("Максимальное количество свободных кресел перед местом", ans_max_places)
