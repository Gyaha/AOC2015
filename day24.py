from itertools import combinations
from math import prod


def read_data(data: str) -> list:
    return [int(a) for a in data.splitlines()]


def find_combos(data: str, div: int):
    d = read_data(data)
    t = sum(d) // div
    comb = []
    for i in range(1, len(d)):
        for c in combinations(d, i):
            if sum(c) == t:
                comb.append(c)
        if len(comb) > 0:
            break
    comb.sort(key=prod)

    return prod(comb[0])


with open("input24") as file:
    data = file.read()
    print(find_combos(data, 3))
    print(find_combos(data, 4))
