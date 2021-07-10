def count_visited_houses(s: str) -> int:
    x, y = 0, 0
    v = set([(0, 0)])
    for l in s:
        if l == "<":
            x -= 1
        elif l == ">":
            x += 1
        elif l == "^":
            y += 1
        else:
            y -= 1
        v.add((x, y))
    return len(v)


def count_visited_with_robot(s: str) -> int:
    sx, sy, rx, ry = 0, 0, 0, 0
    robot = False
    v = set([(0, 0)])
    for l in s:
        if robot:
            rx, ry = move(rx, ry, l)
            v.add((rx, ry))
        else:
            sx, sy = move(sx, sy, l)
            v.add((sx, sy))
        robot = not robot
    return len(v)


def move(x: int, y: int, c: str) -> tuple([int, int]):
    if c == "<":
        x -= 1
    elif c == ">":
        x += 1
    elif c == "^":
        y += 1
    else:
        y -= 1
    return x, y


with open("input03") as file:
    data = file.read()
    print(count_visited_houses(data))
    print(count_visited_with_robot(data))
