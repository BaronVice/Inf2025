

# В текстовом файле разделители должны быть пробелы, а дробь .

f = open("Путь\\до\\файла.txt").readlines()

cluster1 = []
cluster2 = []

for pair in f:
    x,y = map(float, pair.split())
    
    if y < 8: cluster1.append([x, y])
    else: cluster2.append([x, y])

def dist(p1, p2): # расстояние между двумя точками вычисляется по формуле
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def get_centroid(cluster):
    min_dist = 10**9 
    min_point = -1
    for p in cluster: # для каждой точки в кластере
        p_dist = 0
        for neighbor in cluster:
            p_dist += dist(p, neighbor) # считается ее расстояние до остальных
        if p_dist < min_dist: # и если оно меньше текущего минимума
            min_dist = p_dist
            min_point = p # то переопределение центроида

    return min_point

"""
Для файла А определите координаты центра каждого кластера, затем найдите два числа:
Px – минимальную из абсцисс центров кластеров и Py – минимальную из ординат центров кластеров.
"""

centroid1 = get_centroid(cluster1)
centroid2 = get_centroid(cluster2)

print(min(centroid1[0], centroid2[0]) * 10000) # 38471.735
print(min(centroid1[1], centroid2[1]) * 10000) # 61225.014

# Ответ для A: 38471 61225
