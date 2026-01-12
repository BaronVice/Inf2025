

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

lines = open("D:\\vscode\\Inf2025\\Inf2025\\_27\\demo2026\\DEMO_27_A.txt").readlines()

points = []
for line in lines:
    s = line.split()
    points.append([float(s[0]), float(s[1])])

cluster1 = []
cluster2 = []

for point in points:
    if point[1] > 10: cluster1.append(point)
    else: cluster2.append(point)

centroid1 = centroid(cluster1)
centroid2 = centroid(cluster2)

min_x = min(centroid1[0], centroid2[0])
min_y = min(centroid1[1], centroid2[1])

print(min_x * 10000, min_y * 10000)

