def read_shop(s: str):
    wep, arm, rin = [], [None], [None]
    current = None
    for l in s.splitlines():
        if "Weapons:" in l:
            current = wep
        elif "Armor:" in l:
            current = arm
        elif "Rings:" in l:
            current = rin
        else:
            ll = l.split()
            if len(ll) == 0:
                continue
            current.append((int(ll[len(ll) - 3]), int(ll[len(ll) - 2]), int(ll[len(ll) - 1])))
    return wep, arm, rin


def read_boss(s: str):
    hp, dmg, arm = 0, 0, 0
    for l in s.splitlines():
        ll = l.split()
        if "Hit" == ll[0]:
            hp = int(ll[2])
        elif "Damage:" == ll[0]:
            dmg = int(ll[1])
        elif "Armor:" == ll[0]:
            arm = int(ll[1])
    return hp, dmg, arm


def cheap_boss_fight(shop: str, boss: str):
    wep, arm, rin = read_shop(shop)
    b_hp, b_dmg, b_arm = read_boss(boss)
    comb = []
    prices = []
    populate_combinations(wep, arm, rin, comb)
    for c in comb:
        if test_comb(c[0], c[1], c[2], c[3], b_hp, b_dmg, b_arm):
            prices.append(price_comb(c))
    prices.sort()
    return prices[0]


def exp_boss_loss(shop: str, boss: str):
    wep, arm, rin = read_shop(shop)
    b_hp, b_dmg, b_arm = read_boss(boss)
    comb = []
    prices = []
    populate_combinations(wep, arm, rin, comb)
    for c in comb:
        if not test_comb(c[0], c[1], c[2], c[3], b_hp, b_dmg, b_arm):
            prices.append(price_comb(c))
    prices.sort(reverse=True)
    return prices[0]


def test_comb(p_w, p_m, p_r1, p_r2, b_h, b_d, b_a):
    p_h = 100
    p_d = p_w[1] + (0 if p_m == None else p_m[1]) + (0 if p_r1 == None else p_r1[1]) + (0 if p_r2 == None else p_r2[1])
    p_a = p_w[2] + (0 if p_m == None else p_m[2]) + (0 if p_r1 == None else p_r1[2]) + (0 if p_r2 == None else p_r2[2])

    while True:
        b_h -= max(1, p_d - b_a)
        if b_h <= 0:
            return True
        p_h -= max(1, b_d - p_a)
        if p_h <= 0:
            return False


def price_comb(comb: list) -> int:
    p = 0
    for i in range(len(comb)):
        if not comb[i] == None:
            p += comb[i][0]
    return p


def populate_combinations(wep: list, arm: list, rin: list, comb: list):
    for w in wep:
        for a in arm:
            for r1 in rin:
                for r2 in rin:
                    if r1 == None:
                        if not r2 == None:
                            continue
                    else:
                        if r1 == r2:
                            continue
                    comb.append((w, a, r1, r2))


shop = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"""


with open("input21") as file:
    data = file.read()
    print(cheap_boss_fight(shop, data))
    print(exp_boss_loss(shop, data))
