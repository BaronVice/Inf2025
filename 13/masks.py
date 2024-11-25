# Возможные значения масок (первая половина битов 1, вторая 0)
masks = [255 - sum([2**j for j in range(0, i)]) for i in range(0, 9)]
print(masks)