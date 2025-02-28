f = open("Inf2025\\_27\\27.21.B_19715.txt")
points = []

for line in f:
    point = list(map(float, line.split()))
    points.append(point)

cluster1 = []
cluster2 = []
cluster3 = []
cluster4 = []

for point in points:
    x = point[0]
    y = point[1]
    if -20 >= x > -100 and 80 > y > -20 or -10 > x >= -20 and 60 > y > 0:
        cluster1.append(point)
    elif 90 > x > 0 and 100 > y > 0:
        cluster2.append(point)
    elif 0 > x > -100 and -30 > y > -120:
        cluster3.append(point)
    elif 100 > x > 0 and -10 > y > -110:
        cluster4.append(point)


def dist(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5

def get_centroid(cluster):
    p_min = []
    d_min = 10**10
    for p1 in cluster:
        d = 0
        for p2 in cluster:
            d += dist(p1, p2)
        if d < d_min:
            p_min = p1
            d_min = d

    return p_min


c1 = get_centroid(cluster1)
c2 = get_centroid(cluster2)
c3 = get_centroid(cluster3)
c4 = get_centroid(cluster4)

print((c1[0] + c2[0] + c3[0] + c4[0]) / 4 * 10000)
print((c1[1] + c2[1] + c3[1] + c4[1]) / 4 * 10000)
