
# Первое число в файле - количество деталей. Его пропускаем [1:]
f = open("_26\\Производство_деталей\\26_23208.txt").readlines()[1:]

details = []
for i in range(len(f)):
    # все 2N чисел, обозначающих время окрашивания и шлифовки для N деталей
    n1, n2 = map(int, f[i].split())
    # в details будут лежать массивы из [n, t, o]
    # n - время
    # t - тип времени (шлифовка - 1, окрашивание - 2)
    # o - номер детали
    # i + 1 т.к. i с 0, но нумерация деталей с 1
    details.append([n1, 1, i + 1])
    details.append([n2, 2, i + 1])

# упорядочивают по возрастанию
details.sort()

lenta_start = [] # Здесь будут детали, которые по алгоритму размещают с начала ленты
lenta_end = [] # Здесь будут детали, которые по алгоритму размещают с конца ленты
last_detail_o = -1 # номер последней детали, для которой будет определено её место на ленте

visited = set()
for detail in details:
    n = detail[0]
    t = detail[1]
    o = detail[2]
    if o in visited: # если число обозначает время уже рассмотренной детали
        continue # то его не принимают во внимание

    visited.add(o) # иначе рассматривают
    last_detail_o = o

    if t == 1: # если шлифовка, то в начало
        lenta_start.append(detail)
    else: # иначе это окрашивание - в конец
        lenta_end.append(detail)

print(last_detail_o) # первый ответ - номер последней детали
# Если последняя расмотренная деталь расположена на первое свободное место с начала (lenta_start)
if lenta_start[-1][2] == last_detail_o:
    # то до нее будут обработаны все в lenta_start, кроме нее
    print(len(lenta_start) - 1) 
# Иначе последняя расмотренная деталь расположена на первое свободное место с конца (lenta_end)
else:
    # и она будет обработана первой после всех в lenta_start
    print(len(lenta_start)) 

# Ответ: 503 478

# Или проще: 
# lenta_end не нужно т.к. ответ зависит только от lenta_start (можно доказать, но не буду)
# n нужно было только для сортировки на первом шаге
# вместо lenta_start количество, 
# с last_detail_o держать last_detail_t

lenta_start = 0
last_detail_o = -1
last_detail_t = -1

visited = set()
for detail in details:
    t = detail[1]
    o = detail[2]
    if o in visited:
        continue

    visited.add(o)
    last_detail_o = o
    last_detail_t = t

    if t == 1:
        lenta_start += 1

print(last_detail_o)
print(lenta_start - (last_detail_t == 1)) 
