"""
Пример решения 9 задания через python:
# https://inf-ege.sdamgia.ru/problem?id=58476

В каждой строке электронной таблицы записаны шесть натуральных чисел.
Определите количество строк таблицы, содержащих числа, для которых одновременно выполнены все следующие условия:
— максимальное число встречается в строке ровно один раз;
— хотя бы одно число в строке повторяется более одного раза;
— максимальное число в строке превышает среднее арифметическое всех остальных чисел этой строки более чем в три раза.

В ответе запишите число — количество строк, для которых выполнены эти условия.

Шаг 1: откроем excel файл
Шаг 2: Ctrl + A
Шаг 3: Ctrl + C
Шаг 4: Создадим папку, в которой будут лежать файлы a.py и 9.txt
Шаг 5: В 9.txt сделаем Ctrl + V
Шаг 6: Переходим в a.py
"""

# Пусть это файл a.py

answer = 0
for line in open('Inf2025\\9\\9.txt'):
    # В line лежат числа через таб
    nums = [int(num) for num in line.split()]
    # — максимальное число встречается в строке ровно один раз;
    condition_1 = nums.count( max(nums) ) == 1
    # — хотя бы одно число в строке повторяется более одного раза;
    condition_2 = sum([nums.count(el) > 1 for el in nums]) >= 1
    # — максимальное число в строке превышает среднее арифметическое всех остальных чисел этой строки более чем в три раза.
    condition_3 = max(nums) > (sum(nums)/len(nums)) * 3

    if condition_1 and condition_2 and condition_3:
        answer += 1

print(answer)