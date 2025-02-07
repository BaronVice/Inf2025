f = open('Inf2025\\Разборы_вариантов\\Демо\\_27\\demo_2025_27_Б.txt')
f.readline() # пропускаем первую строку, поскольку там "X	                 Y"

data = [tuple(map(float, s.replace(',','.').split())) for s in f]
cluster1 = []
cluster2 = []
cluster3 = []

# Раскидываем точки по кластерам
for point in data:
    px = point[0]
    py = point[1]
    if py <= 3:
        cluster1.append(point)
    elif py <= 7:
        cluster2.append(point)
    else:
        cluster3.append(point)

# Евклидово расстояние между точками p1 и p2
def dist(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5
def get_centroid(cluster):
    dists = [] # здесь будут лежать пары: [сумма от точки p1 до всех остальных, p1]
    for p1 in cluster: # для каждой точки в кластере
        dists += [(sum(dist(p1, p2) for p2 in cluster), p1)] # считаем сумму расстояний от p1 до остальных точек в кластере
    return min(dists)[1] # и выбираем точку с минимальным расстоянием до других

ans = [get_centroid(cluster1), get_centroid(cluster2), get_centroid(cluster3)]
# Это для файла A, где два кластера
#print((ans[0][0] + ans[1][0]) / 2 * 10000, (ans[0][1] + ans[1][1]) / 2 * 10000)
# Это для файла B, где три кластера
print((ans[0][0] + ans[1][0] + ans[2][0]) / 3 * 10000, (ans[0][1] + ans[1][1] + ans[2][1]) / 3 * 10000)