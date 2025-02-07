f = open("Inf2025\\_27\\27.17.B_19566.txt")
f.readline()
data = [tuple(map(float, i.replace(',', '.').split())) for i in f]
cluster1 = []
cluster2 = []
cluster3 = []
cluster4 = []
def s(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

def edge(cluster):
    dists = [] # здесь будут лежать пары: [сумма от точки p1 до всех остальных, p1]
    for p1 in cluster: # для каждой точки в кластере
        dists += [(sum(s(p1, p2) for p2 in cluster), p1)] # считаем сумму расстояний от p1 до остальных точек в кластере
    return max(dists)[1] # и выбираем точку с максимальным расстоянием до других

for point in data:
    x = point[0]
    y = point[1]
    c1 = (-13 <= x <= -7 and 9 <= y <= 17) or (x >= -7 and x <= 13 and y >= 9 and y <= 23)
    c2 = (x >= 13 and x <= 40 and y >= 17 and y <= 32)
    c3 = (x >= -17 and x <= -8 and y >= -9 and y <= 2) or (x >= -8 and x <= 4 and y >= -9 and y <= 5) or (x >= 4 and x <= 7 and y >= -9 and y <= -5) # //
    c4 = (x >= 6 and x <= 31 and y >= -4 and y <= 9.5)
    if c1: cluster1.append(point)
    elif c2: cluster2.append(point)
    elif c3: cluster3.append(point)
    elif c4: cluster4.append(point)
ans = [edge(cluster1), edge(cluster2), edge(cluster3), edge(cluster4)]
print((ans[0][0] + ans[1][0] + ans[2][0] + ans[3][0]) / 4, (ans[0][1] + ans[1][1] + ans[2][1] + ans[3][1]) / 4)















# 10011101.11011100.1011100|1.11101101
# 10011101.11011100.1011100|0.11100110
# 11111111.11111111.1111111|0.00000000
# 10011101.11011100.1011100|0.00000000


