# TODO Найдите количество книг, которое можно разместить на дискете

def solve():
    bytes_has = 1.44 * 1024 * 1024
    bytes_need = 100 * 50 * 25 * 4
    return int(bytes_has // bytes_need)
print("Количество книг, помещающихся на дискету:", solve())
