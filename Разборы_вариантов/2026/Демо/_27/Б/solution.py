

# В текстовом файле разделители должны быть пробелы, а дробь .

f = open("Путь\\до\\файла.txt").readlines()

cluster1 = []
cluster2 = []
cluster3 = []

for pair in f:
    x,y = map(float, pair.split())
    if not(6 <= x <= 26): continue
    
    if y < 18: cluster1.append([x, y])
    elif x < 18: cluster2.append([x, y])
    else: cluster3.append([x, y])

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
Для файла Б определите координаты центра каждого кластера, затем найдите два числа:
Q1 – расстояние между центрами кластеров с минимальным и максимальным количеством точек
и Q2 – максимальное расстояние от центра кластера до точки этого же кластера среди всех кластеров
"""

centroid1 = get_centroid(cluster1)
centroid2 = get_centroid(cluster2)
centroid3 = get_centroid(cluster3)

# Q1
to_sort = [[len(cluster1), centroid1], [len(cluster2), centroid2], [len(cluster3), centroid3]]
to_sort.sort()
min_centroid = to_sort[0][1]
max_centroid = to_sort[-1][1]
print(dist(min_centroid, max_centroid) * 10000) # 142058.77467975824

# Q2
max_dist1 = 0
max_dist2 = 0
max_dist3 = 0
for p in cluster1:
    max_dist1 = max(max_dist1, dist(p, centroid1))
for p in cluster2:
    max_dist2 = max(max_dist2, dist(p, centroid2))
for p in cluster3:
    max_dist3 = max(max_dist3, dist(p, centroid3))

print(max(max_dist1, max_dist2, max_dist3) * 10000) # 25299.751856733765

# Ответ: 142058 25299
