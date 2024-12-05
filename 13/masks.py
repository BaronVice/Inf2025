# Возможные значения масок (первая половина битов 1, вторая 0)
# 0 не беру, поскольку он учитывается в masks
mask_values = [255 - sum([2**j for j in range(0, i)]) for i in range(0, 8)]
print(mask_values)

# А здесь всевозможные значения масок (34 штуки)
# Маски 255.255.255.255 (0 адресов) и 0.0.0.0 (все адреса IpV4) тоже нужно рассматривать.
masks = [[255, 255, 255, i] for i in mask_values
         ] + [[255, 255, i, 0] for i in mask_values
              ] + [[255, i, 0, 0] for i in mask_values
                   ] + [[i, 0, 0, 0] for i in mask_values
                        ] + [[0, 0, 0, 0]]

for i in range(len(masks)):
    print(i+1, masks[i])