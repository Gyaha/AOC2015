SIZE = 1000


def light_matrix(s: str) -> int:
    m = [[False for i in range(SIZE)] for i in range(SIZE)]
    for l in s.splitlines():
        light_instruction(m, l)
    t = 0
    for a in m:
        t += sum(a)
    return t


def light_instruction(m: list, l: str):
    sl = l.split()
    if sl[0] == "turn":
        sx, sy = sl[2].split(",")
        ex, ey = sl[4].split(",")

        light_turn(m, sl[1] == "on", int(sx), int(sy), int(ex), int(ey))
    else:
        sx, sy = sl[1].split(",")
        ex, ey = sl[3].split(",")

        light_toggle(m, int(sx), int(sy), int(ex), int(ey))


def light_turn(m: list, on: bool, sx, sy, ex, ey):
    for y in range(sy - 1, ey):
        for x in range(sx - 1, ex):
            m[y][x] = on


def light_toggle(m: list, sx, sy, ex, ey):
    for y in range(sy - 1, ey):
        for x in range(sx - 1, ex):
            m[y][x] = not m[y][x]


with open("input06") as file:
    data = file.read()
    print(light_matrix(data))
