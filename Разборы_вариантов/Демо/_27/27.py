f = open('Inf2025\\Разборы_вариантов\\Демо\\_27\\demo_2025_27_Б.txt')
f.readline() # пропускаем первую строку, поскольку там "X	                 Y"

data = [tuple(map(float, s.replace(',','.').split())) for s in f]
clusters = []

def dist(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5
def get_centroid(cluster):
    dists = [] # здесь будут лежать пары: [сумма от точки p1 до всех остальных, p1]
    for p1 in cluster: # для каждой точки в кластере
        dists += [(sum(dist(p1, p2) for p2 in cluster), p1)] # считаем сумму расстояний от p1 до остальных точек в кластере
    return min(dists)[1] # и выбираем точку с минимальным расстоянием до других

# DBSCAN impl.
eps = 1
while data: # пока есть точки на распределение распределяем
    clusters.append([data.pop()]) # взяли точку из данных и добавили ее в новый кластер
    for p1 in clusters[-1]: # далее, для точек в кластере
        neighbours = [p2 for p2 in data if dist(p1,p2) < eps] # ищем соседние
        # - Точка является соседней, если расстояние до нее (в этом задании - Евклидово) меньше eps.
        clusters[-1] += neighbours # Добавляем соседей в текущий кластер
        for p in neighbours: data.remove(p) # Рассмотренные точки удаляем
    # И так кластер наполняется, пока есть соседи. 
    # Если же соседей нет, но точки на рассмотрение остались, то их в новый кластер

print("Количество кластеров:", len(clusters))
ans = [get_centroid(cluster) for cluster in clusters]
# Это для файла A, где два кластера
# print((ans[0][0] + ans[1][0]) / 2 * 10000, (ans[0][1] + ans[1][1]) / 2 * 10000)
# Это для файла B, где три кластера
print((ans[0][0] + ans[1][0] + ans[2][0]) / 3 * 10000, (ans[0][1] + ans[1][1] + ans[1][2]) / 3 * 10000)
