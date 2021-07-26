class Player():
    def __init__(self, hp, mana, effects: list = [0, 0, 0]) -> None:
        self.hp = hp
        self.mana = mana
        self.effects = effects

    def copy(self):
        return Player(self.hp, self.mana, self.effects.copy())


class Boss():
    def __init__(self, hp, damage) -> None:
        self.hp = hp
        self.damage = damage

    def copy(self):
        return Boss(self.hp, self.damage)


def cast_spell(spell: int, p: Player, b: Boss) -> int:
    if spell == 0:
        p.mana -= 53
        b.hp -= 4
        return 53
    elif spell == 1:
        p.mana -= 73
        b.hp -= 2
        p.hp += 2
        return 73
    elif spell == 2:
        p.mana -= 113
        p.effects[0] = 6
        return 113
    elif spell == 3:
        p.mana -= 173
        p.effects[1] = 6
        return 173
    elif spell == 4:
        p.mana -= 229
        p.effects[2] = 5
        return 229


def can_cast_spell(spell: int, p: Player) -> bool:
    if spell == 0:
        return p.mana >= 53
    elif spell == 1:
        return p.mana >= 73
    elif spell == 2:
        return p.mana >= 113 and p.effects[0] <= 1
    elif spell == 3:
        return p.mana >= 173 and p.effects[1] <= 1
    elif spell == 4:
        return p.mana >= 229 and p.effects[2] <= 1


def handle_effects(p: Player, b: Boss):
    if p.effects[1] > 0:
        p.effects[1] -= 1
        b.hp -= 3
    if p.effects[2] > 0:
        p.effects[2] -= 1
        p.mana += 101


def handle_shield(p: Player):
    if p.effects[0] > 0:
        p.effects[0] -= 1


def check_status(used: int, wins: list, p: Player, b: Boss):
    if p.hp <= 0 or p.mana <= 0:
        return True
    if b.hp <= 0:
        wins.append(used)
        return True
    return False


def do_boss_damage(p: Player, b: Boss):
    if p.effects[0] > 0:
        p.hp -= b.damage - 7
    else:
        p.hp -= b.damage


def do_next_turn(hard: bool, used: int, wins: list, p: Player, b: Boss):
    if len(wins) and used > min(wins):
        return

    # Hard mode
    if hard:
        p.hp -= 1
        if check_status(used, wins, p, b):
            return
    for spell in range(5):
        if can_cast_spell(spell, p):
            do_turn(hard, used, wins, spell, p.copy(), b.copy())


def do_turn(hard: bool, used: int, wins: list, spell: int, p: Player, b: Boss):
    # Player
    handle_effects(p, b)
    handle_shield(p)
    if check_status(used, wins, p, b):
        return
    used += cast_spell(spell, p, b)
    if check_status(used, wins, p, b):
        return
    # Boss
    handle_effects(p, b)
    if check_status(used, wins, p, b):
        return
    do_boss_damage(p, b)
    handle_shield(p)
    if check_status(used, wins, p, b):
        return

    do_next_turn(hard, used, wins, p, b)


def find_winnings_comboes(hard: bool):
    p = Player(50, 500)
    b = Boss(51, 9)
    wins = []
    do_next_turn(hard, 0, wins, p, b)
    return min(wins)


print(find_winnings_comboes(False))
print(find_winnings_comboes(True))
