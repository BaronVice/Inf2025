
def dist(p1, p2):
    return ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)**0.5
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
def get_main_centroid(raw_points, centroids):
    p_min = []
    d_min = 10**10
    for p in raw_points:
        d = 0
        for c in centroids:
            d += dist(p, c)
        if d < d_min:
            p_min = p
            d_min = d
    return p_min

def dbscan(arr, min_dist):
    clusters = []
    neighbors = []

    while len(arr) != 0:
        clusters.append([])
        neighbors.append(arr[0])
        arr.pop(0)
        while len(neighbors) != 0:
            point = neighbors.pop()
            clusters[-1].append(point)
            for potential in arr:
                if dist(point, potential) < min_dist:
                    neighbors.append(potential)
                    arr.remove(potential)
    return clusters

def solve(file_path):
    # В файле дробь обозначена как , -> для чтения надо предварительно заменить на . (Ctrl+F в файле и замена)
    f = open(file_path) # Откроем файл А

    r,k = -1,-1
    raw_points = []
    for line in f:
        if k == -1:
            r,k = list(map(float, line.split()))
            # в dbscan ... < r, ... <= k
            k += 0.000000001 # мне было лень описывать отдельный случай для k, поэтому применил такое решение
            continue

        point = list(map(float, line.split()))
        raw_points.append(point)

    clusters = dbscan(raw_points.copy(), k)
    points = []
    for cluster in clusters:
        if len(cluster) != 1: points.extend(cluster)

    # print(len(raw_points), len(points))

    clusters = dbscan(points.copy(), r)
    centroids = [get_centroid(cluster) for cluster in clusters]
    main_centroid = get_main_centroid(points, centroids)

    print(int(main_centroid[0] * 10000), int(main_centroid[1] * 10000))

solve("Inf2025\\_27\\hard\\27_A_18390.txt")
solve("Inf2025\\_27\\hard\\27_B_18390.txt")