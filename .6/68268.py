# https://inf-ege.sdamgia.ru/problem?id=68268

# Это задача, в которой сперва надо нарисовать фигуру, затем по этой фигуре
# найти формулу для вычисления

x = 0
while (4*x - 1)**2 - 2*(x*(2*x-3)) <= 1500:
    x += 1
print(x)