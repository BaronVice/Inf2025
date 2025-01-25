# https://inf-ege.sdamgia.ru/problem?id=47226

# id процессов
ids = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12
]
# Их время выполнения
p_time = [
    4,
    3,
    1,
    7,
    6,
    3,
    1,
    2,
    7,
    8,
    6,
    6
]
# От чего они зависят
depends = [
    [0],
    [0],
    [1, 2],
    [3],
    [3],
    [5],
    [4, 6],
    [7],
    [0],
    [0],
    [9],
    [10]
]

# Сделаем dict для удобного получения времени по id
id_time = dict()
for i in range(len(ids)):
    id_time[ids[i]] = p_time[i]

# Сделаем dict для удобного получения зависимостей по id
id_depends = dict()
for i in range(len(ids)):
    id_depends[ids[i]] = depends[i]

# Здесь для каждого процесса будет лежать время выполнения с учетом зависимых
results = dict()
def f(id):
    # return если уже посчитали
    if id in results: return

    # Результат - собственное время выполнение + максимальное из зависимостей (не сумма, поскольку их выполнение параллельно)
    results[id] = id_time[id]
    # Получаем максимальное время, среди зависимостей
    maxx = 0
    for el in id_depends[id]: 
        if el != 0: # 0 - не зависит от других
            f(el)
            maxx = max(maxx, results[el])
            
    results[id] += maxx

# Запустим
for id in ids:
    f(id)

# "Определите минимальное время, через которое завершится выполнение всей совокупности процессов..."
# Ответ - максимальное из всех время
print(max(results.values()))


