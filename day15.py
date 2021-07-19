def read_rules(s: str) -> list:
    rules = []
    for l in s.splitlines():
        ll = l.split()
        rules.append((int(ll[2][:-1]), int(ll[4][:-1]), int(ll[6][:-1]), int(ll[8][:-1]), int(ll[10])))
    return rules


def rec_build_cookie_variations(m: int, n: int, p: list = [], c: list = [], l: int = 1):
    if n == l:
        c.append(m - sum(c))
        p.append(c)
        return
    for i in range(m - (n - l) - sum(c)):
        c2 = c.copy() + [i]
        rec_build_cookie_variations(m, n, p, c2, l + 1)


def find_cookies(s: str):
    rules = read_rules(s)
    v = []
    rec_build_cookie_variations(100, len(rules), v)
    c = []
    for i in range(len(v)):
        c.append(rate_cookie(rules, v[i]))
    c.sort(reverse=True)
    return c[0]


def rate_cookie(rules: list, amounts: list) -> int:
    t = 1
    for p in range(4):
        pp = rate_prop(rules, p, amounts)
        if pp <= 0:
            return 0
        t *= pp
    return t


def rate_prop(rules: list, prop: int, amounts: list):
    t = 0
    for i in range(len(amounts)):
        t += amounts[i] * rules[i][prop]
    return t


def find_calorie_cookie(s: str):
    rules = read_rules(s)
    v = []
    rec_build_cookie_variations(100, len(rules), v)
    c = []
    for i in range(len(v)):
        if rate_prop(rules, 4, v[i]) == 500:
            c.append(rate_cookie(rules, v[i]))
    c.sort(reverse=True)
    return c[0]


def count_calories(rules: list, amounts: list):
    t = 0
    for i in range(len(amounts)):
        t += amounts[i] * rules[i][4]
    return t


with open("input15") as file:
    data = file.read()
    print(find_cookies(data))
    print(find_calorie_cookie(data))
