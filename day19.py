# Note. I am not happy with the b solution.
# Takes ages, but does give the right answer.


def read_data(s: str):
    data1, data2 = [], ""
    for l in s.splitlines():
        if "=>" in l:
            ll = l.split()
            data1.append([list(ll[0]), list(ll[2])])
        elif len(l) > 0:
            data2 = list(l)
    return (data1, data2)


def count_possible_singles(s: str) -> int:
    repl, targ = read_data(s)
    posi = set()
    for r in repl:
        craft_possibles(targ, r, posi)
    return len(posi)


def craft_possibles(targ: list, repl: list, posi: set):
    for i in range(len(targ)):
        if check_spot(targ, i, repl[0]):
            posi.add("".join(craft_spot(targ, repl, i)))


def craft_spot(targ: list, repl: list, i: int):
    return targ[:i] + repl[1] + targ[i + len(repl[0]):]


def check_spot(targ: list, pos: int, s: list):
    for i in range(len(s)):
        if pos + i >= len(targ):
            return False
        if not targ[pos + i] == s[i]:
            return False
    return True


def boil_down_to_single(s: str, targ: str) -> int:
    targ = list(targ)
    repl, current = read_data(s)
    posi = []
    rec_boil(targ, current, repl, posi, 0, set())
    posi.sort()
    return posi[0]


def rec_boil(targ: list, current: list, repl: list, posi: list, step: int, cache: set):
    if current == targ:
        posi.append(step)
        return
    c = "".join(current)
    if c in cache:
        return
    cache.add(c)

    for i in range(len(current)):
        for j in range(len(repl)):
            if check_spot(current, i, repl[j][1]):
                rec_boil(targ, current[:i] + repl[j][0] + current[i + len(repl[j][1]):], repl, posi, step + 1, cache)


with open("input19") as file:
    data = file.read()
    print(count_possible_singles(data))
    print(boil_down_to_single(data, "e"))
