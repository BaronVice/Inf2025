
def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5


def dbscan(arr):
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
                if dist(point, potential) < 1:
                    neighbors.append(potential)
                    arr.remove(potential)
    return clusters

f = open("Inf2025\\_27\\hard\\27_A_20168.txt").readlines()
arr = []
for p in f:
    arr.append(list(map(float, p.split())))

clusters = [el for el in dbscan(arr) if len(el) >= 20]
c = clusters[0]
l = len(clusters[0])
for el in clusters:
    if len(el) < l:
        c = el
        l = len(el)

