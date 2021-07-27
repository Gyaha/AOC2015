def get_next(i: int, c: int, r: int):
    i = (i * 252533) % 33554393
    if r == 1:
        r = c + 1
        c = 1
    else:
        r -= 1
        c += 1
    return i, c, r


i, c, r = 20151125, 1, 1

while True:
    i, c, r = get_next(i, c, r)
    if c == 3075 and r == 2981:
        break
print(i)
