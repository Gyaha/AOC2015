def read_data(s: str) -> list:
    data = []
    for l in s.splitlines():
        data.append([1 if a == "#" else 0 for a in l])
    return data


def take_step(lights: list) -> list:
    new_lights = [["x" for _ in range(len(lights[0]))] for _ in range(len(lights))]
    for y in range(len(lights)):
        for x in range(len(lights[0])):
            c = lights[y][x]
            a = count_around(lights, y, x)
            if c:
                if a == 2 or a == 3:
                    new_lights[y][x] = 1
                else:
                    new_lights[y][x] = 0
            else:
                if a == 3:
                    new_lights[y][x] = 1
                else:
                    new_lights[y][x] = 0
    return new_lights


def draw_lights(lights):
    for l in lights:
        print("".join(["#" if a else "." for a in l]))


def count_around(lights, y, x) -> int:
    n = 0
    n += count_x_y(lights, y - 1, x + 1)
    n += count_x_y(lights, y - 1, x)
    n += count_x_y(lights, y - 1, x - 1)
    n += count_x_y(lights, y + 1, x + 1)
    n += count_x_y(lights, y + 1, x)
    n += count_x_y(lights, y + 1, x - 1)
    n += count_x_y(lights, y, x + 1)
    n += count_x_y(lights, y, x - 1)
    return n


def count_x_y(lights, y, x) -> int:
    if x < 0 or x >= len(lights[0]) or y < 0 or y >= len(lights):
        return 0
    return lights[y][x]


def count_on_after_x(s: str, t: int) -> int:
    lights = read_data(s)
    for _ in range(t):
        lights = take_step(lights)
    n = 0
    for l in range(len(lights)):
        n += sum(lights[l])
    return n


def set_corners_on(lights: list):
    h, w = len(lights) - 1, len(lights[0]) - 1
    lights[0][0] = 1
    lights[h][0] = 1
    lights[0][w] = 1
    lights[h][w] = 1


def count_on_after_x_broken(s: str, t: int) -> int:
    lights = read_data(s)
    set_corners_on(lights)
    for _ in range(t):
        lights = take_step(lights)
        set_corners_on(lights)
    n = 0
    for l in range(len(lights)):
        n += sum(lights[l])
    return n


with open("input18") as file:
    data = file.read()
    print(count_on_after_x(data, 100))
    print(count_on_after_x_broken(data, 100))
