from itertools import permutations


def read_rules(s: str) -> dict:
    rules = {}
    for l in s.splitlines():
        try:
            ll = l.split()
            name, numb, targ = ll[0], int(ll[3]), ll[10][:-1]
            if not ll[2] == "gain":
                numb = -numb
            if not name in rules.keys():
                rules[name] = []
            rules[name].append((targ, numb))
        except:
            print(l)
    return rules


def rank_seatings(s: str) -> int:
    rules = read_rules(s)
    a = rules.keys()
    n = 0
    for b in permutations(a, len(a)):
        m = rank_seating(rules, b)
        if m > n:
            n = m
    return n


def rank_seating(rules: dict, seats: list) -> int:
    n = 0
    for i in range(len(seats)):
        rule = rules[seats[i]]
        if i == 0:
            left, right = seats[len(seats) - 1], seats[i + 1]
        elif i == len(seats) - 1:
            left, right = seats[i - 1], seats[0]
        else:
            left, right = seats[i - 1], seats[i + 1]
        for r in rule:
            if r[0] == left or r[0] == right:
                n += r[1]
    return n


with open("input13") as file:
    data = file.read()
    print(rank_seatings(data))
    print(rank_seatings(data + "Me 0 0 0 0 0 0 0 0 0 0"))
