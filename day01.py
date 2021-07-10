

def find_floor(s: str) -> int:
    floor = 0
    for l in s:
        if l == "(":
            floor += 1
        else:
            floor -= 1
    return floor


def find_basement(s: str) -> int:
    floor = 0
    position = 0
    for l in s:
        position += 1
        if l == "(":
            floor += 1
        else:
            floor -= 1
        if floor < 0:
            break
    return position


with open("input01.txt") as file:
    data = file.readline()
    print(find_floor(data))
    print(find_basement(data))
