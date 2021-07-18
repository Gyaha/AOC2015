def read_rules(s: str) -> dict:
    def add_rule(rules: dict, f: str, t: str, d: int):
        if not f in rules.keys():
            rules[f] = []
        rules[f].append((d, t))
    rules = {}
    for l in s.splitlines():
        r, d = l.split(" = ")
        r1, r2 = r.split(" to ")
        dist = int(d)
        add_rule(rules, r1, r2, dist)
        add_rule(rules, r2, r1, dist)
    return rules


def calculate_x_route(s: str, longest: bool) -> int:
    rules = read_rules(s)
    routes = []
    rec_find_routes(rules, list(rules.keys()), [], routes)
    dists = []
    calc_dists(rules, routes, dists)
    dists.sort(reverse=longest)
    return dists[0]


def calc_dists(rules: dict, routes: list, dists: list):
    for ro in routes:
        d = 0
        for i in range(len(ro) - 1):
            f, t = ro[i], ro[i + 1]
            for ru in rules[f]:
                if ru[1] == t:
                    d += ru[0]
        dists.append(d)


def rec_find_routes(rules: dict, a: list, visited: list, routes: list):
    if len(a) == len(visited):
        routes.append(visited)
        return
    for i in a:
        if i in visited:
            continue
        v = visited.copy()
        v.append(i)
        rec_find_routes(rules, a, v, routes)


with open("input09") as file:
    data = file.read()
    print(calculate_x_route(data, False))
    print(calculate_x_route(data, True))
