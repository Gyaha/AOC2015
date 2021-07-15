def bits_and_bops(s: str, target: str) -> int:
    rules = {}
    for l in s.splitlines():
        r, t = l.split(" -> ")
        rl = r.split()
        if len(rl) == 1:
            rules[t] = ["REF"] + rl
        elif len(rl) == 2:
            rules[t] = rl
        else:
            rules[t] = [rl[1], rl[0], rl[2]]
    return bit16_to_int(rec_get_value(rules, target, {}))


def rec_get_value(rules: dict, s: str, cache: dict) -> list:
    if s in cache.keys():
        return cache[s]
    if s.isnumeric():
        return int_to_16bit(int(s))
    rule = rules[s]
    v = None
    if rule[0] == "REF":
        v = rec_get_value(rules, rule[1], cache)
    elif rule[0] == "NOT":
        v = b_not(rec_get_value(rules, rule[1], cache))
    elif rule[0] == "AND":
        v = b_and(rec_get_value(rules, rule[1], cache), rec_get_value(rules, rule[2], cache))
    elif rule[0] == "OR":
        v = b_or(rec_get_value(rules, rule[1], cache), rec_get_value(rules, rule[2], cache))
    elif rule[0] == "LSHIFT":
        v = b_lshift(rec_get_value(rules, rule[1], cache), rec_get_value(rules, rule[2], cache))
    elif rule[0] == "RSHIFT":
        v = b_rshift(rec_get_value(rules, rule[1], cache), rec_get_value(rules, rule[2], cache))
    cache[s] = v
    return v


def int_to_16bit(i: int) -> list:
    return [int(v) for v in bin(i)[2:].zfill(16)]


def bit16_to_int(v: list) -> int:
    return int("".join([str(a) for a in v]), 2)


def b_not(i: list) -> list:
    n = [0 for _ in range(16)]
    for j in range(len(i)):
        if i[j] == 0:
            n[j] = 1
        else:
            n[j] = 0
    return n


def b_and(i: list, j: list) -> list:
    n = [0 for _ in range(16)]
    for k in range(len(i)):
        if i[k] and j[k]:
            n[k] = 1
        else:
            n[k] = 0
    return n


def b_or(i: list, j: list) -> list:
    n = [0 for _ in range(16)]
    for k in range(len(i)):
        if i[k] or j[k]:
            n[k] = 1
        else:
            n[k] = 0
    return n


def b_lshift(i: list, j: list) -> list:
    x = min(bit16_to_int(j), 16)
    if x == 0:
        return i
    return i[x:] + [0 for _ in range(x)]


def b_rshift(i: list, j: list) -> list:
    x = min(bit16_to_int(j), 16)
    if x == 0:
        return i
    return [0 for _ in range(x)] + i[:-x]


with open("input07") as file:
    data = file.read()
    print(bits_and_bops(data, "a"))
    print(bits_and_bops(data + "46065 -> b", "a"))
