from itertools import combinations


def read_data(s: str) -> list:
    data = []
    for l in s.splitlines():
        data.append(int(l))
    data.sort()
    return data


def find_storage_variants(s: str, t: int) -> int:
    containers = read_data(s)
    n = 0
    for i in range(1, len(containers)):
        for p in combinations(containers, i):
            if sum(p) == t:
                n += 1
    return n


def find_storage_row(s: str, t: int) -> int:
    containers = read_data(s)
    l = find_lowest_possible_row(containers, t)
    n = 0
    for p in combinations(containers, l):
        if sum(p) == t:
            n += 1
    return n


def find_lowest_possible_row(containers: list, t: int) -> int:
    for i in range(1, len(containers)):
        for p in combinations(containers, i):
            if sum(p) == t:
                return i


with open("input17") as file:
    data = file.read()
    print(find_storage_variants(data, 150))
    print(find_storage_row(data, 150))
