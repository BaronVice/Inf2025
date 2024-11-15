# https://inf-ege.sdamgia.ru/problem?id=48433
# Здесь по аналогии с https://github.com/BaronVice/Inf2025/blob/main/12/35901.py

minn = 10000000

for x in range(0, 100):
    for y in range(0, 100):
        for z in range(0, 100):
            for v in range(0, 100):
                # Условие про единицы в полученной строке: y + 2*v == 40
                # Условие про двойки в полученной строке: x + 2*z > 50
                # Условие про равенство единиц и двоек в исходной строке: 2 * x + z == 2 * y + v
                if y + 2*v == 40 and x + 2*z > 50 and 2 * x + z == 2 * y + v:
                    minn = min(minn, x + 2*z)
print(minn)