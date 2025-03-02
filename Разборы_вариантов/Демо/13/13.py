"""
В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
какая часть IP-адреса узла сети относится к адресу сети, а какая – к адресу узла в этой сети.
Адрес сети получается в результате применения поразрядной конъюнкции к заданному адресу узла и маске сети.

Сеть задана IP-адресом 172.16.168.0 и маской сети 255.255.248.0.
Сколько в этой сети IP-адресов, для которых количество единиц в двоичной записи IP-адреса не кратно 5?

В ответе укажите только число.
"""

# Перепишем в битовом представлении адрес сети и маску
# С того бита, где у маски начинаются нули, начинаются адреса узлов сети.

# 172.16.168.0  - 10101100.00010000.10101|000.00000000
# 255.255.248.0 - 11111111.11111111.11111|000.00000000

# Из чего количество адресов = 2**количество_0_в_маске = 2**11 = 2048
# Количество 1 в адресе узла = Количество 1 в адресе сети + количество 1 в битовой записи номера узла

ans = 0
# Перебор каждого номера узла
for i in range(2048):
    net = 8 # в сети количество единиц = 8 (10101100.00010000.10101|000.00000000)
    bin_node = bin(i).count('1') # находим количество единиц у номера узла
    # Важно! Если считать нужно 0, то запись будет следующая: 8 - bin(i)[2:].count('1')
    # Связано это с тем, что ведущие нули для нас важны и первые два символа, обозначающие систему счисления, содержат 0
    # Например при bin(16) получим '0b10000'
    if (net + bin_node) % 5 != 0: ans += 1

print(ans)
