def read_rules(s: str) -> list:
    rules = []
    for l in s.splitlines():
        ll = l.split()
        rules.append([int(ll[1][:-1]), {
            ll[2][:-1]:int(ll[3][:-1]),
            ll[4][:-1]:int(ll[5][:-1]),
            ll[6][:-1]:int(ll[7])}])
    return rules


keys = {"children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1}

keys2 = {"children": ["=", 3],
         "cats": [">", 7],
         "samoyeds": ["=", 2],
         "pomeranians": ["<", 3],
         "akitas": ["=", 0],
         "vizslas": ["=", 0],
         "goldfish": ["<", 5],
         "trees": [">", 3],
         "cars": ["=", 2],
         "perfumes": ["=", 1]}


def find_the_right_sue(s: str, keys: dict) -> int:
    rules = read_rules(s)
    for sue in rules:
        if check_sue(sue, keys):
            return sue[0]


def find_the_real_sue(s: str, keys: dict) -> int:
    rules = read_rules(s)
    for sue in rules:
        if real_check_sue(sue, keys):
            return sue[0]


def real_check_sue(sue: list, keys) -> bool:
    for ru in sue[1].keys():
        b = sue[1][ru]
        a = keys[ru]
        if a[0] == "=":
            if not a[1] == b:
                return False
        elif a[0] == "<":
            if not a[1] > b:
                return False
        else:
            if not a[1] < b:
                return False
    return True


def check_sue(sue: list, keys: dict) -> bool:
    for ru in sue[1].keys():
        a = keys[ru]
        b = sue[1][ru]
        if not a == b:
            return False
    return True


with open("input16") as file:
    data = file.read()
    print(find_the_right_sue(data, keys))
    print(find_the_real_sue(data, keys2))
