

def dist(point, neighbour):
    x1 = point[0]
    x2 = neighbour[0]
    y1 = point[1]
    y2 = neighbour[1]
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def centroid(cluster):
    min_point = [12.34, 56.78]
    min_dist = 10**9
    for point in cluster:
        d = 0
        for neighbour in cluster:
            d += dist(point, neighbour)
        if d < min_dist:
            min_dist = d
            min_point = point

    return min_point

lines = open("file_destination").readlines()

points = []
for line in lines:
    s = line.split()
    points.append([float(s[0]), float(s[1])])

cluster1 = []
cluster2 = []
cluster3 = []

for point in points:
    if point[0] < 5 or 30 < point[0]: continue

    if point[0] > 18: cluster1.append(point)
    elif point[1] > 20: cluster2.append(point)
    else: cluster3.append(point)

centroid1 = centroid(cluster1)
centroid2 = centroid(cluster2)
centroid3 = centroid(cluster2)

l1 = len(cluster1)
l2 = len(cluster2)
l3 = len(cluster3)

# Задача со звездочкой: дописать
