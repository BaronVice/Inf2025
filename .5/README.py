# Преобразование из десятичного в двоичную:
# функция bin(n) вернет число n в двоичном представлении, при условии что n десятичное.
a = 123
a_bin_pref = bin(a) # -> "0b1111011"
# Получаем строку такого типа.
# Приставка 0b нам не нужна, чтобы получить без нее добавим срез:
a_bin = bin(a)[2:] # -> "1111011", также строка

# Преобразование из двоичного числа в десятичную:
# Функция int(n, 2) вернет число n в десятичном представлении, при условии что n двоичное
b_int = int(a_bin_pref, 2) # -> 123, можно с префиксом
b_int = int(a_bin, 2) # -> 123, а можно и без
# Главное, чтобы давалась сттрока в двоичном представлении

print("a:", a)
print("a_bin_pref:", a_bin_pref)
print("a_bin:", a_bin)
print("b_int:", b_int)

